from twilio.rest import TwilioRestClient

account_sid = "ACb1e4fdef43eb2e0f6fac05377c12acb3" # Your Account SID from www.twilio.com/console
auth_token  = "5d10532e84c1afa5a51a37ec095180af"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+46706798574",    # Replace with your phone number
    from_="+46844682686") # Replace with your Twilio number

print(message.sid)