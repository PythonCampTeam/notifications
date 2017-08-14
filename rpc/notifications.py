from nameko.rpc import rpc
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content
# import urllib.request as urllib
from twilio.rest import Client
# from datetime import datetime
#from keys import SENDGRID_API_KEY
# import json
# from nameko.events import EventDispatcher, event_handler
# from config.settings.common import security


class Notifications(object):
    """This class make Notifications request
        """
    name = 'NotificationsRPC'

    #sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

    # def __init__(self):
    #     self.sendgrid_key = SENDGRID_API_KEY
    #     #self.sendgrid_v2_client = sendgrid.SendGridAPIClient(self.sendgrid_key)
    #     self.sendgrid_v3_client = sendgrid.SendGridAPIClient(apikey=self.sendgrid_key)

    @rpc
    def testing(self, **kwargs):
        doc_class = self.__dict__
        return {self.__class__.__name__: doc_class,
                'docs': self.__class__.__doc__}

    @rpc
    def send_email(self, to_email='test@example.com'):
        """This method send email to customer
        Args:
            to_email (str) : email of customer
        """
        SENDGRID_API_KEY = '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'
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        from_email = Email("test@example.com")
        #to_email = Email("test@example.com")
        to_email = Email(to_email)
        subject = "Notifications about Order"
        content = Content("text/plain", "Orders")
        mail = Mail(from_email, subject, to_email, content)
        #response = sg.client.mail.send.post(request_body=mail.get())
        sg.client.mail.send.post(request_body=mail.get())
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        return "Messages send"

    @rpc
    def send_sms(self, number):
        """This method send sms to customer
        Args:
            number (str) : number of customer
        """
        accaunt_sid = 'AC3adbfe0e72f9d7dc7197fefd2cab7aca'
        auth_token = 'f3ab11d8839c7752d07db9854b93bc8f'
        client = Client(accaunt_sid, auth_token)
        client.messages.create(
                to=number,
                from_='+16195866444',
                body='Na potolke nosok!'
                )
        return 'message send'

    # @rpc
    # def send_email2(self, to_email, from_email, subject, body_html, body_text):
    #
    #     message = sendgrid.Mail(to=to_email, subject=subject, html=body_html,
    #                             text=body_text, from_email=from_email)
    #     print("SENDGRID: send_email: Attempting to send email to {to_email} from {from_email}
    #     with subject {subject} at time {time}".format(
    #         to_email=to_email,
    #         from_email=from_email,
    #         subject=subject,
    #         time=datetime.now(),
    #         ))
    #     status, msg = self.sendgrid_v3_client.send(message)
    #     response = Notifications.sg.client.mail.send.post(message)
    #     print("SENDGRID: send_email: Received response from Sendgrid at time {time} with status {status}
    #      and response {msg}".format(
    #         time=datetime.now(),
    #         status=status,
    #         msg=msg,
    #         ))
    #     return response
