# import os
# from dotenv import load_dotenv
# import praw

# load_dotenv()

# reddit = praw.Reddit(
#     client_id=os.getenv('REDDIT_CLIENT_ID'),
#     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
#     user_agent=os.getenv('REDDIT_USER_AGENT')
# )

# print("\n=== Connection Test ===")
# print(f"Client ID: {reddit.config.client_id}")
# print(f"User Agent: {reddit.config.user_agent}")
# print(f"Read Only: {reddit.read_only}")

# try:
#     # Test API call
#     subreddit = reddit.subreddit('all')
#     for post in subreddit.hot(limit=1):
#         print(f"\nFirst post in r/all: {post.title}")
#     print("✅ API call successful!")
# except Exception as e:
#     print(f"\n❌ Error: {type(e).__name__} - {str(e)}")
#     print("Possible solutions:")
#     print("- Regenerate API credentials")
#     print("- Check Reddit API status: https://www.redditstatus.com/")
#     print("- Verify account email is verified")