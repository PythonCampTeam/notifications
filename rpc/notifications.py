from nameko.rpc import rpc
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content
# import urllib.request as urllib
from twilio.rest import Client
from nameko.timer import timer
# from datetime import datetime
# from keys import SENDGRID_API_KEY
# import json
# from nameko.events import EventDispatcher, event_handler
#from notifications.config.settings.common import security as security_settings


class Notifications(object):
    """This class make Notifications request
        """
    name = 'NotificationsRPC'

    # sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

    @rpc
    def testing(self, **kwargs):
        doc_class = self.__dict__
        return {self.__class__.__name__: doc_class,
                'docs': self.__class__.__doc__}

    @rpc
    #@timer(interval=2)
    def send_email(self, to_email, from_email, subject, content):
        """This method send email to customer with use SenfGrid
        Args:
            to_emails (str) : email of customer
            from_emails(str): email of shop
            subject (str): subject of mail
            content(str): content of the mail
        """
        SENDGRID_API_KEY = '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'
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        from_email = Email(from_email)
        to_email = Email(to_email)
        mail = Mail(from_email, subject, to_email, content)
        content = Content(content)
        # response = sg.client.mail.send.post(request_body=mail.get())
        sg.client.mail.send.post(request_body=mail.get())
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        return "Messages send"

    @rpc
    #@timer(interval=2)
    def send_sms(self, to_phone, content):
        """This method send sms to customer
        Args:
            to_phone (str) : number of customer
            body (str): message to customer
            from(str): number of salary
        """
        accaunt_sid = 'AC3adbfe0e72f9d7dc7197fefd2cab7aca'
        auth_token = 'f3ab11d8839c7752d07db9854b93bc8f'

        client = Client(accaunt_sid, auth_token)
        message = client.messages.create(
                to=to_phone,
                from_='+16195866444',
                body=content
        )
        #return(message.error_code, message.error_message)
