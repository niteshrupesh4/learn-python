from twilio.rest import Client
from API.credentials import account_sid, auth_token, my_cell, my_twilio

account = account_sid
token = auth_token
client = Client(account, token)
my_msg = 'Your message gose here.. OTP 546739'
message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
