import unittest
import sendgrid
import twilio
from unittest import TestCase
from unittest.mock import MagicMock, patch
#from nameko.testing.services import worker_factory
from notifications.rpc.endpoints import Notifications
# from sendgrid.helpers.mail import Content, Email, Mail
#import python_http_client
# def test_conversion_service():
#     service = worker_factory(ConversionService)

# def test_send_email_creates_message_with_correct_data():
#     service = Notifications()
#     sendgrid_mock = MagicMock()
#     send_method_mock = MagicMock()
#     send_method_mock.return_value = ('202')
#     sendgrid_mock.send = send_method_mock
#     service.sg = sendgrid_mock
#
#     with patch('notifications.rpc.notifications.sendgrid.Mail') as mail_mock:
#         service.send_email(
#             to_email="Test Account <test@test.com>",
#             from_email="sendertest@test.com",
#             subject="test subject",
#             body_html="test body html",
#             body_text="test body text",
#             )
#
#         mail_mock.assert_called_once_with(
#             to="Test Account <test@test.com>",
#             subject="test subject",
#             html="test body html",
#             text="test body text",
#             from_email="sendertest@test.com",
#             )


class TestMail(TestCase):

    def setUp(self):
        self.to_email = "tamara.malysheva@saritasa.com"
        self.from_email = "test@example.com"
        self.subject = "blabla"
        self.name = "Shepard"
        self.label = "https://vk.com/studentslifeinsfu"
        self.return_value = {"status code": 202}
        self.sengrid_key = Notifications.sengrid_key
        self.notifications = Notifications()
        self.number = '+79994413746'
        self.content = 'testing'
        self.return_sms = {"error_code": None}
        self.fake_number = '+79994413741'

    # @patch('sendgrid.helpers.mail.Content', return_value='Content')
    # @patch('sendgrid.helpers.mail.Mail', return_value='Mail')
    # @patch('sendgrid.helpers.mail.Email', return_value='test_mail')
    # @patch('sendgrid.SendGridAPIClient', return_value='Client')
    # # @patch('sendgrid.SendGridAPIClient(apikey=self.sengrid_key).client.mail.send.post(request_body=mail.get())', return_value='Mail_send')
    # def test_mail(self, Content_mock, Mail_mock, Email_mock, sendgrid_client):
    #     """Test checks that email will send"""
    #     # sendgrid.SendGridAPIClient = MagicMock(return_value = '202')
    #     # sendgrid.SendGridAPIClient.client.mail.send.post = MagicMock(return_value = '202')
    #     # response = MagicMock(return_value = '202')
    #     # self.assertEqual(Notifications.send_email(self.notifications,
    #     #                                           self.to_email,
    #     #                                           self.label,
    #     #                                           self.from_email,
    #     #                                           self.subject,
    #     #                                           self.name
    #     #                                           ), self.return_value)
    #     print(sendgrid.SendGridAPIClient(apikey='fjaskf123h'))
    #     print(self.notifications.send_email(self.to_email,
    #                                         self.label,
    #                                         self.from_email,
    #                                         self.subject,
    #                                         self.name))

    def test_patch(self):
        """Testing send mail to customer with using mock"""
        service = Notifications()
        sendgrid_mock = MagicMock(return_value='200')
        send_method_mock = MagicMock()
        send_method_mock.return_value = (200, 'some message')
        sendgrid_mock.send = send_method_mock
        Notifications.sendgrid_client = sendgrid_mock

        with patch('sendgrid.helpers.mail.Mail') as mail_mock:
                    service.send_email(
                                       self.to_email,
                                       self.label,
                                       self.from_email,
                                       self.subject,
                                       self.name,
                                    )
                    #mail_mock.assert_not_called()


    #@patch('send_email.response', return_value={"status code": "202"})
    # def test_mail_error(self):
    #     """Test checks error if send empty email of customer"""
    #     sendgrid.SendGridAPIClient = MagicMock(return_value = '202')
    #     client.mail.send.post = MagicMock(return_value = '202')
    #     self.assertNotEqual(Notifications.send_email(self.notifications,
    #                                                  1,
    #                                                  self.label,
    #                                                  self.from_email,
    #                                                  self.subject,
    #                                                  self.name
    #                                                  ), self.return_value)

    # def test_mail_error(self):
    #     """Test checks error if send empty email of customer"""
    #
    #     self.assertNotEqual(Notifications.send_email(self.notifications,
    #                                                 1,
    #                                                 self.label,
    #                                                 self.from_email,
    #                                                 self.subject,
    #                                                 self.name
    #                                                 ), self.return_value)

    def test_sms(self):
        """Test checks sms sending"""
        service = Notifications()
        twilio_mock = MagicMock()
        send_method_mock = MagicMock()
        send_method_mock.return_value = (200, 'some message')
        twilio_mock.send = send_method_mock
        Notifications.client = twilio_mock
        twilio.rest.Client = MagicMock()
        twilio.rest.Client.messages.create = MagicMock(return_value=self.return_sms)
        with patch('twilio.rest.Client') as sms_mock:
            self.assertNotEqual(service.send_sms(
                                                self.number, self.content
                                                ), self.return_sms)

            self.assertNotEqual(service.send_sms(
                                                   self.fake_number,
                                                   self.content
                                                   ), self.return_sms)



if __name__ == '__main__':
    unittest.main()
