import unittest
from unittest import TestCase

from notifications.db.database_notification import Store


class TestMail(TestCase):

    def setUp(self):
        self.sms_db = Store()
        self.mail_db = Store()
        self.mail_data = {"status": "Ok", "time": "date of send"}
        self.mail = 'test@example.com'
        self.number = '+1656565656'
        self.sid = '2454544564646'
        Store.add_mail(self.mail_db, self.mail, self.mail_data)
        Store.add_sms(self.sms_db, self.number, self.sid)

    def test_add_mail(self):
        """Cheks that mail add"""
        Store.add_mail(self.mail_db, self.mail, self.mail_data)

    def test_add_sms(self):
        """Cheks that sms info add"""
        Store.add_sms(self.sms_db, self.number, self.sid)

    def test_return_sms(self):
        """Check that db return sms"""
        print(Store.get_sms(self.sms_db))

    def test_return_mail(self):
        """Check that db return sms"""
        print(Store.get_mail(self.mail_db))

    def test_clear(self):
        """Cheks remove db"""
        Store.clear_db(self.sms_db)
        Store.clear_db(self.mail_db)


if __name__ == '__main__':
    unittest.main()
