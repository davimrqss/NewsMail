import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from keys import news_api_key

# Fetch news articles using NewsAPI for given languages and search term
def get_news_newsapi(search_languages, search_term, days_back):
    url = 'https://newsapi.org/v2/everything'
    from_date = datetime.now() - timedelta(days=days_back)
    all_articles = []

    for lang in search_languages:
        params = {
            'apiKey': news_api_key,
            'q': search_term,
            'language': lang,
            'pageSize': 20,
            'from': from_date.strftime('%Y-%m-%d')
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            articles = response.json()
            valid_articles = [
                article for article in articles.get('articles', [])
                if article.get('title') and 'removed' not in article['title'].lower()
            ]
            all_articles.extend(valid_articles)
        else:
            print(f"API request error for language '{lang}': {response.status_code}")

    return all_articles

# Extract plain text from an article URL (limited to 200 characters)
def extract_full_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join(p.get_text() for p in paragraphs)
            return text[:200] + '...' if len(text) > 200 else text
        return 'Content not available.'
    except Exception as e:
        print(f"Error extracting content from {url}: {str(e)}")
        return 'Content not available.'
