import unittest
import sendgrid
from unittest import TestCase
#from unittest.mock import MagicMock, patch
#from nameko.testing.services import worker_factory
from rpc.endpoints import Notifications
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
#
#
class TestMail(TestCase):

    def setUp(self):
        self.to_email = "tamara.malysheva@saritasa.com"
        self.from_email = "test@example.com"
        self.subject = "blabla"
        self.name = "Shepard"
        self.label = "https://vk.com/studentslifeinsfu"
        self.return_value = {"status code": 202}
        self.sengrid_key = Notifications.sengrid_key
        self.sg = Notifications.sg
        self.notifications = Notifications()
        self.number = '+79994413746'
        self.content = 'testing'
        self.return_sms = {"error_code": None}
        self.fake_number = '+79994413741'

    # @patch('Notifications.send_email', return_value={"status code": "202"})
    def test_mail(self):
        self.assertEqual(Notifications.send_email(self.notifications,
                                                  self.to_email,
                                                  self.label,
                                                  self.from_email,
                                                  self.subject,
                                                  self.name
                                                  ), self.return_value)
        self.assertNotEqual(Notifications.send_email(self.notifications,
                                                     1,
                                                     self.label,
                                                     self.from_email,
                                                     self.subject,
                                                     self.name
                                                     ), self.return_value)

    def test_sms(self):
        print(Notifications.send_sms(self.notifications,
                                                self.number, self.content
                                                ),
                                                self.return_sms)
        self.assertEqual(Notifications.send_sms(self.notifications,
                                                self.number, self.content
                                                ), self.return_sms)
        print
        self.assertNotEqual(Notifications.send_sms(self.notifications,
                                                   self.fake_number,
                                                   self.content
                                                   ), self.return_sms)


if __name__ == '__main__':
    unittest.main()
