# sentiment_analysis.py

from textblob import TextBlob

def analyze_sentiment(articles):
    positive, neutral, negative = 0, 0, 0
    for article in articles:
        blob = TextBlob(article['title'] + " " + article.get("description", ""))
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            positive += 1
        elif sentiment == 0:
            neutral += 1
        else:
            negative += 1

    total = positive + neutral + negative
    return {
        "positive": positive,
        "neutral": neutral,
        "negative": negative,
        "support_score": (positive - negative) / total if total else 0
    }
