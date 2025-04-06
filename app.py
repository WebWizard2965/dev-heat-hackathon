import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import praw
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import joblib

app = Flask(__name__)
load_dotenv()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

def analyze_topics(texts, n_topics=3):
    """Train or load LDA model for topic analysis"""
    try:
        # Try loading existing model
        vectorizer = joblib.load('model/vectorizer.joblib')
        lda = joblib.load('model/lda.joblib')
    except:
        # First-time training
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        X = vectorizer.fit_transform(texts)
        lda = LatentDirichletAllocation(n_components=n_topics)
        lda.fit(X)
        
        os.makedirs('model', exist_ok=True)
        joblib.dump(vectorizer, 'model/vectorizer.joblib')
        joblib.dump(lda, 'model/lda.joblib')
    
    # Predict topics
    X = vectorizer.transform(texts)
    topic_dist = lda.transform(X)
    return {
        'posts': texts,
        'topics': [{
            'keywords': [vectorizer.get_feature_names_out()[i] 
                       for i in topic.argsort()[:-6:-1]]
        } for topic in lda.components_],
        'assignments': topic_dist.argmax(axis=1)
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    trends = None
    error = None
    
    if request.method == 'POST':
        try:
            num_posts = min(int(request.form.get('num_posts', 10)), 50)
            
            # Fetch Reddit posts
            posts = [post.title for post in reddit.subreddit('all').hot(limit=num_posts)]
            
            # Analyze topics
            trends = analyze_topics(posts)
            
        except Exception as e:
            error = f"Error analyzing trends: {str(e)}"
    
    return render_template('index.html', trends=trends, error=error)

if __name__ == '__main__':
    app.run(debug=True)