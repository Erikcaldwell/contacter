from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with contact information via SMS."""
    # getting the body of the message
    body = request.values.get('Body', None)

    # Start our response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'Connect':
        resp.message("Here is my contact info:\nErik Caldwell\nDeputy Chief Operating Officer\nSmart and Sustainable Communities Branch\nCity of San Diego\nPhone: (619) 235-5880\necaldwell@sandiego.gov\nLinkedIn: https://www.linkedin.com/in/erikcaldwell/\nTwitter: @erikcaldwell")
    elif body == 'connect':
        resp.message("Here is my contact info:\nErik Caldwell\nDeputy Chief Operating Officer\nSmart and Sustainable Communities Branch\nCity of San Diego\nPhone: (619) 235-5880\necaldwell@sandiego.gov\nLinkedIn: https://www.linkedin.com/in/erikcaldwell/\nTwitter: @erikcaldwell")
    elif body == 'Connect ':
        resp.message("Here is my contact info:\nErik Caldwell\nDeputy Chief Operating Officer\nSmart and Sustainable Communities Branch\nCity of San Diego\nPhone: (619) 235-5880\necaldwell@sandiego.gov\nLinkedIn: https://www.linkedin.com/in/erikcaldwell/\nTwitter: @erikcaldwell")
    elif body == 'connect ':
        resp.message("Here is my contact info:\nErik Caldwell\nDeputy Chief Operating Officer\nSmart and Sustainable Communities Branch\nCity of San Diego\nPhone: (619) 235-5880\necaldwell@sandiego.gov\nLinkedIn: https://www.linkedin.com/in/erikcaldwell/\nTwitter: @erikcaldwell")
    else:
        resp.message("This is just a txt msg bot. Call 619-533-5880 if you need to chat or email ecaldwell@sandiego.gov. Thanks!")

    return str(resp)


if __name__ == "__main__":
    #remember to turn off debug before going to prodcution
    app.run(debug=True)
