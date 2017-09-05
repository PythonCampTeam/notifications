import urllib

import cerberus
import sendgrid
import twilio
from nameko.rpc import rpc
from sendgrid.helpers.mail import Content, Email, Mail
from twilio.rest import Client
from jinja2 import Environment, PackageLoader
from notifications.config.settings.common import security as security_settings
from notifications.db.database_notification import Store
from notifications.rpc.shcema import body_mail, body_type

Validator = cerberus.Validator
v = Validator()


class Notifications(object):
    """This class make Notifications request (sms and email)
    with use twillo and sendgrid.

        Args:
            ENV : Environment for loader template.
            template (html): Template for label.
            name (stirng): Name of service

        Attributes:
            subject (string): Subject of mail.
            mail_db (list): Db for customers emails.
            sms_db (list): Db for customers phones.
            sengrid_key (str): Api key of sendgrid.
            sendgrid_client : Client of sendgrid allows send mail.
            client : Client of twilio allows send sms.
            address_from : Mail address of shop.
            from_number (str): Number of shop (twilio number).
            subject (str): Subject of mail.

    """
    ENV = Environment(loader=PackageLoader(
                                    'notifications.config',
                                    'templates'
                                          )
                      )
    template = ENV.get_template('email_template.html')
    name = 'NotificationsRPC'

    def __init__(self):
        self.mail_db = Store()
        self.sms_db = Store()

        self.sengrid_key = ''.join(security_settings.SENDGRID_API_KEY)
        self.sendgrid_client = sendgrid.SendGridAPIClient(
                                    apikey=self.sengrid_key
                                    )
        self.client_twilio = Client(security_settings.accaunt_sid,
                                    security_settings.auth_token)
        self.address_from = 'tamaramalysheva5991@gmail.com'
        self.from_number = security_settings.twilio_number
        self.subject = "Your Order"

    @rpc
    def send_email(self, to_email, label, name):
        """This method send email to customer with use SenfGrid

        Args:
            to_emails (str) : email of customer
            from_emails(str): email of shop
            subject (str): subject of mail
            name (str): name of customer
            label (str): link to label of shipping

        Return:
            response.code (str): return 202 if email sended

        """
        try:
            from_email = Email(self.from_email)
            to_email = Email(to_email)
            content = Content(body_type,
                              body_mail.format(name, label))
            mail = Mail(from_email, self.subject, to_email, content)
            mail.template_id = security_settings.TEMPLATE_ID['PythonCamp']

            response = self.sendgrid_client.client.mail.send.post(
                request_body=mail.get())
        except urllib.error.HTTPError as e:
            return {"HTTPError": e.code}

        self.mail_db.add_mail(to_email, response.headers)
        return {"status": response.status_code}

    def email_content(self, name, label=None, order=None):

        context = {
                    'name': name,
                    'label': label,
                    'order_id': order.id,
                    'order_items': order['items']
                   }
        content = self.template.render(context)

        content = Content('text/html', content)
        return content

    @rpc
    def send_email_with_temp(self, address_to, name, order, label=None, ):
        """This method send email to customer with template.

        Args:
            address_to (str) : email of customer
            label (str): link to label of shipping
            order (dict): order of customer

        Return:
            response.code (str): return 202 if email sended
        """
        address_from = Email(self.address_from)
        to_email = Email(address_to)
        mail = Mail(address_from,
                    self.subject,
                    to_email,
                    self.email_content(name,
                                       label,
                                       order
                                       )
                    )

        response = self.sendgrid_client.client.mail.send.post(
            request_body=mail.get())
        self.mail_db.add_mail(to_email, response.headers)

        return {"status": response.status_code}

    @rpc
    def send_sms(self, number, content="Your Order Ready"):
        """This method send sms to customer
        Args:
            to_phone (str) : number of customer
            content (str): message to customer
            from(str): number of salary (one number in free twillo accaunt)
        Return:
            message.code_error(str): return null if sms send correct
        """
        try:
            message = self.client_twilio.messages.create(
                    to=number,
                    from_=security_settings.twilio_number,
                    body=content
                    )
        except twilio.base.exceptions.TwilioRestException as e:
            return {
                    "code": e.code,
                    "message": e.msg
                    }
        self.sms_db.add_sms(number, message.sid)
        return {"error_code": message.error_code}
