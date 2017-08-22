

class StoreDB(object):
    """
        Class for storing data from Notifications.
        It stored date about email and sms.

        Args:
            element (dict): current element witch added in db
            db_mail (list): list of email date
            db_sms (list): list of sms date

    """
    def __init__(self, **kwargs):
        self.element = {}
        self.db_mail = []
        self.db_sms = []

    def add_mail(self, mail, data):
        """Adde new information about email
        Args:
            email(str): email of customer
            date(str): information about sms notification

        """
        self.element = {"email": mail, "date": data}
        self.db_mail.append(self.element)

    def add_sms(self, number, sid, status):
        """Adde new information about sms
        Args:
            number(str): number of customer
            date(str): information about sms notification

        """
        self.element = {"number": number, "sid": sid,  "status": status}
        self.db_sms.append(self.element)

    def get_item(self):
        return self.db.element

    def clear_db(self):
        """This method clear cart and items"""
        self.db_sms, self.db_mail = []

    def get_mail(self):
        return self.db_mail

    def get_sms(self):
        return self.db_sms
