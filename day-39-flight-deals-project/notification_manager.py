from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("TWL_ID")
TWILIO_AUTH_TOKEN = os.environ.get("SMS_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWL_VIRTUAL_NUM")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWL_VERIFIED_NUM")


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
