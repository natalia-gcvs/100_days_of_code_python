from twilio.rest import Client
import smtplib
import os

TWILIO_SID = os.environ.get("TWL_ID")
TWILIO_AUTH_TOKEN = os.environ.get("SMS_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWL_VIRTUAL_NUM")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWL_VERIFIED_NUM")

my_email = os.environ["smtp_email"]
password = 'ivykmwyixvrlkfum'


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

    def send_emails(self, user_email, user_name, msg):
        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=user_email,
                                msg=f"Subject:Flight Deals\n\n\nDear {user_name},\n{msg}".encode('utf-8'))



