from nameko.rpc import rpc
import cerberus
import sendgrid
from config.settings.common import security as security_settings
from rpc import mail_data
from rpc import sms
from sendgrid.helpers.mail import Content, Email, Mail
from twilio.rest import Client
import twilio

Validator = cerberus.Validator
v = Validator()


class Notifications(object):
    """This class make Notifications request (sms and email)
    with use twillo and sendgrid.

    """

    name = 'NotificationsRPC'

    @rpc
    def send_email(self, request):
        """This method send email to customer with use SenfGrid

        Args:
            to_emails (str) : email of customer
            from_emails(str): email of shop
            subject (str): subject of mail
            body(str): content of the mail

        Return:
            response.code (str): return 202 if email sended

        """
        sengrid_key = ''.join(security_settings.SENDGRID_API_KEY)
        sg = sendgrid.SendGridAPIClient(apikey=sengrid_key)
        if not v.validate(request, mail_data.schema_body):
            return {"errors": v.errors}

        to_email = request.get("to_email", 'tamara.malysheva@saritasa.com')
        from_email = request.get("from_email", 'test@example.com')
        subject = request.get("subject")
        body = request.get("content")

        from_email = Email(from_email)
        to_email = Email(to_email)
        content = Content(mail_data.body_type,
                          mail_data.body_mail.format(body))
        mail = Mail(from_email, subject, to_email, content)
        mail.template_id = security_settings.TEMPLATE_ID['PythonCamp']
        response = sg.client.mail.send.post(request_body=mail.get())
        return response.status_code

    @rpc
    def send_sms(self, body):
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
        if not v.validate(body, sms.schema_sms):
            return {"errors": v.errors}
        to_phone = body.get("to_phone", '+79994413746')
        content = body.get("content", 'Your Order ready')
        try:
            message = client.messages.create(
                    to=to_phone,
                    from_=security_settings.twilio_number,
                    body=content
                    )
        except twilio.base.exceptions.TwilioRestException as e:
            return {
                    "code": "HTTP 400 error",
                    "message":
                    """Unable to create record: The To number is not a valid
                       phone number"""}
        return message.error_code
