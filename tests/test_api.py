import unittest
from unittest import TestCase
from nameko.rpc import rpc, RpcProxy
from unittest.mock import MagicMock, patch
#from notifications import Notifications
import rpc.notifications
from nameko.testing.services import worker_factory


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
        self.body = {
                "to_email": "tamara.malysheva@saritasa.com",
                "from_email": "test@example.com",
                "subject": "blabla",
                "name": "Tamara",
                "label": "https://vk.com/studentslifeinsfu"
                }

    @patch('Notifications.send_email', return_value={"status code": "202"})
    def test_mail(self):
        self.assertEqual(Notifications.send_email(self.body), {"status code": "202"})


if __name__ == '__main__':
    unittest.main()
