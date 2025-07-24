# emails input
print('-' * 10, 'Email', '-' * 10)
emuser_input = input('Enter the email to be used: ')
empass_input = input('Enter the email password: ')
user_input = input('Type the emails to send (space-separeted): ').split() 
print(' ')

print('-' * 10, 'News', '-' * 10)
napikey_input = input('Type your NewsAPI key: ') # Key NewsAPI
print(' ')

# Keys
email_host = 'smtp.gmail.com' # Gmail Server  
email_port = 587 # Port of gmail server
email_user = emuser_input
email_password = empass_input
email_to = user_input 
news_api_key = napikey_input