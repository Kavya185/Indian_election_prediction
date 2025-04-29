# utils.py

from sentiment_analysis import analyze_sentiment
from news_fetchers import fetch_news

def get_party_support(party_list, state=None):
    results = {}
    for party in party_list:
        articles = fetch_news(party, state)
        sentiment = analyze_sentiment(articles)
        results[party] = sentiment
    return results

def get_sorted_support(results):
    return sorted(results.items(), key=lambda x: x[1]['support_score'], reverse=True)
