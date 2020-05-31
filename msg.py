from twilio.rest import Client

account_sid = 'Your Twilio Project ID'
auth_token = 'Your project auth token'
client = Client(account_sid, auth_token)
def send_notice():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Attention Hi Dear!',
                                  to='whatsapp:+919887407475'
                              )

    print(message.sid)
