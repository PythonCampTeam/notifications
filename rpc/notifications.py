from nameko.rpc import rpc
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content
from twilio.rest import Client
# from nameko.timer import timer
from config.settings.common import security as security_settings
import db.database as db


class Notifications(object):
    """This class make Notifications request (sms and email)
    with use twillo and sendgrid.
        """
    name = 'NotificationsRPC'

    mail_db = db.StoreDB(data_stored='address_to', data_key='object_id')
    sms_db = db.StoreDB(data_stored='phone_to', data_key='object_id')

    @rpc
    def docs(self, **kwargs):
        doc_class = self.__dict__
        return {self.__class__.__name__: doc_class,
                'docs': self.__class__.__doc__}

    @rpc
    def send_email(self, to_email, subject, content,
                   from_email='tamara.malysheva@saritasa.com'):
        """This method send email to customer with use SenfGrid
        Args:
            to_emails (str) : email of customer
            from_emails(str): email of shop
            subject (str): subject of mail
            content(str): content of the mail
        Return:
            response.code (str): return 202 if email sended
        """
        SENDGRID_API_KEY =''
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        from_email = Email(from_email)
        to_email = Email(to_email)
        mail = Mail(from_email, subject, to_email, content)
        content = Content(content)
        response = sg.client.mail.send.post(request_body=mail.get())
        self.mail_db.add(to_email)
        return response.status_code

    @rpc
    def send_sms(self, to_phone='+79994413746', content='Your Order ready'):
        """This method send sms to customer
        Args:
            to_phone (str) : number of customer
            body (str): message to customer
            from(str): number of salary (one number in free twillo accaunt)
        Return:
            message.code_error(str): return null if sms send correct
        """

        client = Client(security_settings.accaunt_sid,
                        security_settings.auth_token)
        message = client.messages.create(
                to=to_phone,
                from_=security_settings.twilio_number,
                body=content
        )
        self.sms_db.add(to_phone)
        return message.error_code
