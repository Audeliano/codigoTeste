from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe7aacf2578dbbe1a1eaec546f92c79ba"
# Your Auth Token from twilio.com/console
auth_token  = "66c267074c2e0129e120caa9a075dd3f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5535991531951", 
    from_="+555139370601",
    body="Fala cuzao!!")

print(message.sid)
