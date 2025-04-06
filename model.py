from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import joblib
import os

# Train or load model
def predict_topics(texts, n_topics=5):
    # Load pretrained model if exists
    if os.path.exists('model/topic_model.joblib'):
        model = joblib.load('model/topic_model.joblib')
        vectorizer = joblib.load('model/vectorizer.joblib')
    else:
        # First-time training
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2)
        X = vectorizer.fit_transform(texts)
        model = LatentDirichletAllocation(n_components=n_topics)
        model.fit(X)
        
        # Save for future
        os.makedirs('model', exist_ok=True)
        joblib.dump(model, 'model/topic_model.joblib')
        joblib.dump(vectorizer, 'model/vectorizer.joblib')
    
    # Predict topics
    X = vectorizer.transform(texts)
    topic_dist = model.transform(X)
    
    # Get top keywords per topic
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        topics.append({
            'id': topic_idx,
            'keywords': [feature_names[i] for i in topic.argsort()[:-6:-1]]
        })
    
    return {
        'posts': texts,
        'topics': topics,
        'topic_distribution': topic_dist.argmax(axis=1).tolist()
    }