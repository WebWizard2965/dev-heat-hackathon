# Reddit Trend Spotter 🔥

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey)
![ML](https://img.shields.io/badge/ML-LDA%2FTF--IDF-orange)

Real-time analysis of trending Reddit topics using machine learning.

## Features ✨
- 🕵️ Live Reddit post analysis from /r/all
- 🤖 Automated topic modeling with LDA
- 📊 Interactive topic visualization
- 🔒 Secure API credential management

## Tech Stack 🛠️
```bash
// Python + Flask (Backend)
// PRAW (Reddit API)
// Scikit-learn (ML Pipeline)
// Bootstrap 5 (Frontend) [to-be]
// Joblib (Model Persistence)
```

## Setup 🚀
1. Clone repo:
```bash
git clone https://github.com/WebWizard2965/dev-heat-hackathon.git
cd dev-heat-hackathon
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure `.env`:
```bash
REDDIT_CLIENT_ID="YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET="YOUR_SECRET"
REDDIT_USER_AGENT="web:TrendSpotter:v1.0 (by /u/YOUR_USERNAME)"
```

4. Run:
```bash
python app.py
```

## Usage 📈
1. Visit `http://localhost:5000`
2. Enter post count (1-50)
3. See trends + topics

## License 📜
MIT License - See [LICENSE](LICENSE)

---
> **Note**: Replace placeholder credentials in `.env.example` and rename to `.env`
