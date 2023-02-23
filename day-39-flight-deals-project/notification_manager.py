from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("OWM_KEY_API")
TWILIO_AUTH_TOKEN = os.environ.get("SMS_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+19788506384"
TWILIO_VERIFIED_NUMBER = "+353833126285"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.status)
