from twilio.rest import Client

account_sid = 'AC1ee4d176d6b662e56b89e9a1e136cd0e'
auth_token = '3b6622fc220469011bb2747f6b9e79e9'
client = Client(account_sid, auth_token)
def send_notice():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Attention Rohit!',
                                  to='whatsapp:+919887407475'
                              )

    print(message.sid)
