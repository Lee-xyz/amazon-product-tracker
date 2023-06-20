import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

class EmailSender:
    def __init__(self, EMAIL_ADDRESS, CURRENCY_SYMBOL):
        self.EMAIL_ADDRESS = EMAIL_ADDRESS
        self.CURRENCY_SYMBOL = CURRENCY_SYMBOL

    def notify(self, url, name, rrp, current_price, discount):
        SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(f'Purchase now for {self.CURRENCY_SYMBOL}{current_price} now at {url} for a {discount * 100}% discount (RRP: {self.CURRENCY_SYMBOL}{rrp}).')
        message['to'] = self.EMAIL_ADDRESS
        message['subject'] = f'{name} from Amazon is on sale!'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (service.users().messages().send(userId="me", body=create_message).execute())
            print(F'Sent email to {message}. Message id: {message["id"]}.')
        except HTTPError as error:
            print(f'An error has occurred: {error}')
            message = None