from twilio.rest import Client

account_sid = 'AC1ee4d176d6b662e56b89e9a1e136cd0e'
auth_token = 'b1404c78cafe137a9a8f2bf4a68b0a68'
client = Client(account_sid, auth_token)
def send_notice():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Attention Rohit!',
                                  to='whatsapp:+919887407475'
                              )

    print(message.sid)
