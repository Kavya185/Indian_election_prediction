from gnews import GNews

def fetch_news(party_name, state=None):
    google_news = GNews(language='en', max_results=20)
    query = f"{party_name} election"
    if state:
        query = f"{party_name} {state} election"
    return google_news.get_news(query)
