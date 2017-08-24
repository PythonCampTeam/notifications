import unittest
from rpc.notifications import send_email, send_sms
from nameko.rpc import rpc, RpcProxy
from unittest.mock import MagicMock, patch
from notifications.rpc.notifications import Notifications
from nameko.testing.services import worker_factory


# def test_conversion_service():
#     service = worker_factory(ConversionService)

def test_send_email_creates_message_with_correct_data():
    service = Notifications()
    sendgrid_mock = MagicMock()
    send_method_mock = MagicMock()
    send_method_mock.return_value = ('202')
    sendgrid_mock.send = send_method_mock
    service.sg = sendgrid_mock

    with patch('src.main.sendgrid.Mail') as mail_mock:
        service.send_email(
            to_email="Test Account <test@test.com>",
            from_email="sendertest@test.com",
            subject="test subject",
            body_html="test body html",
            body_text="test body text",
            )

        mail_mock.assert_called_once_with(
            to="Test Account <test@test.com>",
            subject="test subject",
            html="test body html",
            text="test body text",
            from_email="sendertest@test.com",
            )
