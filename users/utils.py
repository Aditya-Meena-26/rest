import random
import string
import requests
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp   
    
def send_email(email,otp):
    api_key = os.getenv("api_key")
    url = 'https://api.sendinblue.com/v3/smtp/email'

    headers = {
        'Content-Type': 'application/json',
        'api-key': api_key
    }

    data = {
        'sender': {
            'name': 'Aditya Meena',
            'email': 'adityameena@thoughtwin.com'
        },
        'to': [
            {
                'email': email
                
            }
        ],
        'subject': 'welcome to our Kisan page',
        'htmlContent': f'<p>Dear User </p>'
                    f'<p>your login OTP is {otp}.<b>'
                    
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code,"-----------------")
    if response.status_code == 201:
        return True
    else:
        return 'Failed to send email.'