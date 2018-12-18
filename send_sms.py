# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
consumer_key = os.environ['account_sid']
consumer_secret = os.environ['auth_token']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18587710266',
                     to='+18582294768'
                 )

print(message.sid)
