import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from keys import email_host, email_port, email_user, email_password

# Send the formatted email to the recipient list
def send_email(subject, body, recipients):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['Subject'] = subject

    # Ask if user wants to add an email signature
    signature_html = ""
    if input("Add a signature? (y/n): ").lower() == 'y':
        print("Type your signature (Press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        signature_html = "<br>".join(f"<p>{line}</p>" for line in lines)

        if input("Add an image to the signature? (y/n): ").lower() == 'y':
            image_url = input("Enter image URL: ")
            signature_html += f'<p><img src="{image_url}" style="height:100px;width:200px;"></p>'

    msg.attach(MIMEText(body + "<br><br>" + signature_html, 'html'))

    server = smtplib.SMTP(email_host, email_port)
    server.starttls()
    server.login(email_user, email_password)

    text = msg.as_string()
    for recipient in recipients:
        msg['To'] = recipient
        server.sendmail(email_user, recipient, text)

    server.quit()

# Format articles into HTML for email body
def format_articles(articles, email_title):
    html = f"<h1>{email_title}</h1>"
    for article in articles:
        summary = article.get('custom_summary', article.get('description', ''))
        html += f"<h2>{article['title']}</h2>"
        html += f"<p>{summary}</p>"
        if article.get('urlToImage'):
            html += f"<img src='{article['urlToImage']}' style='max-width:100%;height:400px;width:800px;'><br>"
        html += "<hr>"
    return html
