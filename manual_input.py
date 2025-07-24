# Manually add a news article via user input
def add_manual_article():
    article = {}
    article['title'] = input("Enter article title: ")
    article['description'] = input("Enter article description: ")
    article['url'] = input("Enter article URL: ")
    article['urlToImage'] = input("Enter image URL (optional): ")
    return article

# Review each article manually, and optionally add summaries or include/exclude
def review_articles_manually(articles):
    selected_articles = []

    for article in articles:
        print('')
        print(f"Title: {article['title']}")
        print(f"Description: {article.get('description', '')}")
        print(f"URL: {article['url']}")
        print(' ')
        include = input("Include this article in the email? (y/n): ")
        if include.lower() == 'y':
            print('')
            custom_summary = input("Enter a custom summary (or leave blank to use the description): ")
            article['custom_summary'] = custom_summary if custom_summary else article.get('description', '')
            selected_articles.append(article)
        print('')
        print("-" * 30)
        print('')

    # Offer to add additional manual articles
    while input("Would you like to add another article manually? (y/n): ").lower() == 'y':
        selected_articles.append(add_manual_article())

    return selected_articles
