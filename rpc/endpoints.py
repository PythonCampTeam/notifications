from nameko.rpc import rpc
import cerberus
import sendgrid
from notifications.config.settings.common import security as security_settings
from notifications.rpc.shcema import body_mail, body_type
from sendgrid.helpers.mail import Content, Email, Mail
from twilio.rest import Client
from notifications.db.database import StoreDB
import twilio
#import python_http_client
import urllib


Validator = cerberus.Validator
v = Validator()


class Notifications(object):
    """This class make Notifications request (sms and email)
    with use twillo and sendgrid.

    """
    mail_db = StoreDB()
    sms_db = StoreDB()
    name = 'NotificationsRPC'
    sengrid_key = ''.join(security_settings.SENDGRID_API_KEY)
    sg = sendgrid.SendGridAPIClient(apikey=sengrid_key)

    @rpc
    def send_email(self, to_email, label, from_email, subject, name):
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
            from_email = Email(from_email)
            to_email = Email(to_email)
            content = Content(body_type,
                              body_mail.format(name, label))
            mail = Mail(from_email, subject, to_email, content)
            mail.template_id = security_settings.TEMPLATE_ID['PythonCamp']
            response = self.sg.client.mail.send.post(request_body=mail.get())
        except urllib.error.HTTPError as e:
            return {"HTTPError": e.code}

        self.mail_db.add_mail(to_email, response.headers)
        return {"status code": response.status_code}

    @rpc
    def send_sms(self, number, content):
        """This method send sms to customer
        Args:
            to_phone (str) : number of customer
            content (str): message to customer
            from(str): number of salary (one number in free twillo accaunt)
        Return:
            message.code_error(str): return null if sms send correct
        """
        client = Client(security_settings.accaunt_sid,
                        security_settings.auth_token)
        # if not v.validate(body, shcema.schema_sms):
        #     return {"errors": v.errors}
        # to_phone = body.get("to_phone", '+79994413746')
        # content = body.get("content", 'Your Order ready')
        try:
            message = client.messages.create(
                    to=number,
                    from_=security_settings.twilio_number,
                    body=content
                    )
        except twilio.base.exceptions.TwilioRestException as e:
            return {
                    "code": "HTTP 400 error",
                    "message":
                    """Unable to create record: The To number is not a valid
                       phone number"""}
        self.sms_db.add_sms(number, message.sid, message.status)
        return {"error_code": message.error_code}