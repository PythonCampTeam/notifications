from nameko.rpc import rpc
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, Content
import urllib.request as urllib
from twilio.rest import Client
from datetime import datetime
from keys import SENDGRID_API_KEY
import json
from nameko.events import EventDispatcher, event_handler
from keys import accaunt_sid, auth_token


class Notifications(object):
    """his class make Notifications request to add cost to trash
    Args:
        name(str): The name  tovar
        aditional(dict): information about tovar
    Return:
        cost(int): PPPPPP
        """
    name = 'NotificationsRPC'
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

    @rpc
    def testing(self, **kwargs):
        doc_class = self.__dict__
        return {self.__class__.__name__: doc_class,
                'docs': self.__class__.__doc__}

    @rpc
    def send_email(self, to_email):
        from_email = Email("test@example.com")
        #to_email = Email("test@example.com")
        to_email = Email(to_email)
        subject = "Notifications about Order"
        content = Content("text/plain", "and easy to do anywhere, even with Python")
        mail = Mail(from_email, subject, to_email, content)
        response = Notifications.sg.client.mail.send.post(request_body=mail.get())
        return response

    @rpc
    def send_sms(self, number):
        client = Client(accaunt_sid, auth_token)
        client.messages.create(
                to='+77017335394',
                from_='+16195866444',
                body='Na potolke nosok!'
                )
        return 'send sms'

    @rpc
    def send_email2(self, to_email, from_email, subject, body_html, body_text):

        message = sendgrid.Mail(to=to_email, subject=subject, html=body_html,
                                text=body_text, from_email=from_email)
        print("SENDGRID: send_email: Attempting to send email to {to_email} from {from_email} with subject {subject} at time {time}".format(
            to_email=to_email,
            from_email=from_email,
            subject=subject,
            time=datetime.now(),
            ))

        status, msg = Notifications.sq.client.send(message)
        response = Notifications.sg.client.mail.send.post(message)
        print("SENDGRID: send_email: Received response from Sendgrid at time {time} with status {status} and response {msg}".format(
            time=datetime.now(),
            status=status,
            msg=msg,
            ))
        return response
