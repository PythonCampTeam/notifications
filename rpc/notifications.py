from nameko.rpc import rpc
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content
from twilio.rest import Client
from nameko.timer import timer
from config.settings.common import security as security_settings
import db.database as db


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

    mail_db = db.StoreDB(data_stored='address_to', data_key='object_id')
    sms_db = db.StoreDB(data_stored='phone_to', data_key='object_id')

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
            response.body (str): contain info about sending email
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
        self.sms_db.add(to_phone)
        # return(message.error_code, message.error_message)
        # return json.dumps(message.body.encode('utf-8'))
        return message.error_code

    # @timer(interval=1)
    # def sprinter_mail(self):
    #     """
    #         method work infinity and check temp db, and take
    #         from temp db max timestamp item
    #     Return:
    #          None
    #     """
    #     #shippo.verify_ssl_certs = False
    #
    #     #shippo.api_key = security_settings.TOKEN_GOSHIPPO['TEST_TOKEN']
    #
    #     test_items = self.mail_db.get_items()
    #     if test_items:
    #         address_to = max(dict(self.mail_db.get_items()))
    #         before_res = self.mail_db.get_item(object_id=address_to)
    #         self.mail_db.delete(object_id=address_to)
    #         result = shippo.Address.create(**before_res)
    #         print(result)
    #         self.store_db.add(result)
    #
    # @timer(interval=1)
    # def sprinter_sms(self):
    #     """
    #         method work infinity and check temp db, and take
    #         from temp db max timestamp item
    #     Return:
    #          None
    #     """
    #
    #     test_items = self.temp_db.get_items()
    #     if test_items:
    #         address_to = max(dict(self.mail_db.get_items()))
    #         before_res = self.mail_db.get_item(object_id=address_to)
    #         self.temp_db.delete(object_id=address_to)
    #         result = shippo.Address.create(**before_res)
    #         print(result)
    #         self.store_db.add(result)
