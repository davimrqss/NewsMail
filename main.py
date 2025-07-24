from news import get_news_newsapi
from manual_input import review_articles_manually, add_manual_article
from email_utils import send_email, format_articles
from keys import email_to

# Get user input for search languages and keywords
print('Available languages: pt / en / ru / es / fr / ar / de / he / it / nl / no / sv / ud / zh')
print(' ')
search_languages = input("Enter the languages to search (space-separated): ").split()
search_term = input("Enter the search term (separeted by 'OR'): ")
email_subject = input("Enter the email subject: ")
article_title = input('Type the title of the article: ')
days_back = input("Enter how many past days to search news from (e.g. 1, 3, 7): ")
try:
    days_back = int(days_back)
except ValueError:
    print("Invalid number. Defaulting to 5 days.")
    days_back = 5
print('')
print("-" * 30)

# Fetch articles from NewsAPI
articles = get_news_newsapi(search_languages, search_term, days_back)

# Check if any articles were found
if articles:
    reviewed_articles = review_articles_manually(articles)
else:
    print("No automatic articles found.")
    reviewed_articles = []
    while input("Would you like to add an article manually? (y/n): ").lower() == 'y':
        reviewed_articles.append(add_manual_article())

# If articles were selected or added, proceed
if reviewed_articles:
    email_body = format_articles(reviewed_articles, article_title)
    if input("Send email now? (y/n): ").lower() == 'y':
        send_email(email_subject, email_body, email_to)
        print("Emails sent successfully.")
else:
    print("No articles selected to send.")
