from nameko.rpc import rpc
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content
from twilio.rest import Client
from nameko.timer import timer
from notifications.config.settings.common import security as security_settings


class Notifications(object):
    """This class make Notifications request (sms and email)
    with use twillo and sendgrid.
        """
    name = 'NotificationsRPC'

    @rpc
    def docs(self, **kwargs):
        doc_class = self.__dict__
        return {self.__class__.__name__: doc_class,
                'docs': self.__class__.__doc__}

    @rpc
    @timer(interval=2)
    def send_email(self, to_email, from_email, subject, content):
        """This method send email to customer with use SenfGrid
        Args:
            to_emails (str) : email of customer
            from_emails(str): email of shop
            subject (str): subject of mail
            content(str): content of the mail
        Return:
            response.body (str): contain info about sending email
        """

        sg = sendgrid.SendGridAPIClient(apikey=
                                        security_settings.SENDGRID_API_KEY)
        from_email = Email(from_email)
        to_email = Email(to_email)
        mail = Mail(from_email, subject, to_email, content)
        content = Content(content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return response.body

    @rpc
    @timer(interval=2)
    def send_sms(self, to_phone, content):
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
        # return(message.error_code, message.error_message)
        # return json.dumps(message.body.encode('utf-8'))
        return message.error_code
