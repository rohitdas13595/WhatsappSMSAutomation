from twilio.rest import Client

account_sid = 'Your Twilio Project ID'
auth_token = 'Your project auth token'
client = Client(account_sid, auth_token)
def send_notice():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Attention Hi Dear!',
                                  to='whatsapp:phone_no with_countrycode'
                              )

    print(message.sid)
