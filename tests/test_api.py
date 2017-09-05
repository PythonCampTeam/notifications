import unittest
from unittest import TestCase
from unittest.mock import MagicMock
import stripe

import twilio

from helpers_for_test import Mail, Messages
from notifications.rpc.endpoints import Notifications


class TestMail(TestCase):

    def setUp(self):
        self.to_email = "tamara.malysheva@saritasa.com"
        self.from_email = "test@example.com"
        self.subject = "blabla"
        self.name = "Shepard"
        self.label = "https://vk.com/studentslifeinsfu"
        self.return_value = {"status code": 202}
        self.number = '+79994413746'
        self.content = 'testing'
        self.return_sms = {"error_code": None}
        self.fake_number = '+79994413741'
        self.url = 'localhost/8000'
        self.msg = 'HTTP Error'
        self.code = '101'
        self.msg = 'Test error message'
        self.hdrs = 'Test'
        self.fp = 'Test'
        self.items = [{
                      "amount": 1500,
                      "currency": "usd",
                      "description": "Test",
                      "object": "order_item",
                      "parent": "sku_BLBV7Osb2fUo0W",
                      "quantity": 1,
                      "type": "sku"},
                      {
                      "amount": 0,
                      "currency": "usd",
                      "description": "Taxes (included)",
                      "object": "order_item",
                      "parent": "null",
                      "quantity": "null",
                      "type": "tax"},
                      {
                        "amount": 0,
                        "currency": "usd",
                        "description": "Free shipping",
                        "object": "order_item",
                        "parent": "ship_free-shipping",
                        "quantity": "null",
                        "type": "shipping"
                          }]
        self.order = {"id": "1",
                      "items": self.items
                      }
        self.order1 = stripe.StripeObject().construct_from(
                              self.order, '')

    def test_mail_patch(self):
        """Testing send mail to customer with using mock"""
        service = Notifications()
        mail = Mail()
        service.sendgrid_client = MagicMock(return_value='200')
        method = service.sendgrid_client
        method.client.mail.send.post = MagicMock(return_value=mail)
        self.assertEqual(service.send_email(
                                self.to_email,
                                self.label,
                                self.name,
                                    ), {'status': '200'})

    def test_mail__with_template_patch(self):
        """Testing send mail to customer with using mock"""
        service = Notifications()
        mail = Mail()
        service.sendgrid_client = MagicMock(return_value='200')
        method = service.sendgrid_client
        method.client.mail.send.post = MagicMock(return_value=mail)
        self.assertEqual(service.send_email_with_temp(
                                self.to_email,
                                self.name,
                                self.label,
                                self.order1,
                                    ), {'status': '200'})

    def test_sms(self):
        """Test checks sms sending"""
        service = Notifications()
        message = Messages()
        service.sms_db.add_sms = MagicMock(return_value='added')
        service.client_twilio.messages.create = MagicMock(return_value=message)
        print(service.send_sms(self.number, self.content))
        self.assertNotEqual(service.send_sms(
                                            self.number,
                                            self.content
                                            ), self.return_sms)

        self.assertNotEqual(service.send_sms(
                                            self.fake_number,
                                            self.content

                                            ), self.return_sms)

    def test_sms_exs(self):
        """Test checks sms exseption"""
        status = 'sdsd'
        uri = 'nfjshr7t7g/bbf/3'
        side_effect = twilio.base.exceptions.TwilioRestException(
            code=self.code,
            status=status,
            msg=self.msg,
            uri=uri)
        service = Notifications()
        service.sms_db.add_sms = MagicMock(return_value='added')
        service.client_twilio.messages.create = MagicMock(side_effect=side_effect)
        print(service.send_sms('4454545', self.content))

    def test_mail_exs(self):
        service = Notifications()
        print(service.send_email(
                                1,
                                self.label,
                                self.name,
                                    ))
        self.assertNotEqual(service.send_email(
                                1,
                                self.label,
                                self.name,
                                    ), {'status': '200'})


if __name__ == '__main__':
    unittest.main()
