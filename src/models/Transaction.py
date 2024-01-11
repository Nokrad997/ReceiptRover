class Transaction:
    def __init__(self, transaction_id, user_id, date, scan_id, key):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.date = date
        self.scan_id = scan_id
        self.key = key

    @property
    def get_transaction_id(self):
        return self.transaction_id

    @property
    def get_user_id(self):
        return self.user_id

    @property
    def get_date(self):
        return self.date

    @property
    def get_scan_id(self):
        return self.scan_id

    @property
    def get_key(self):
        return self.key

    @get_transaction_id.setter
    def set_transaction_id(self, value):
        self.transaction_id = value

    @get_user_id.setter
    def set_user_id(self, value):
        self.user_id = value

    @get_date.setter
    def set_date(self, value):
        self.date = value

    @get_scan_id.setter
    def set_scan_id(self, value):
        self.scan_id = value

    @get_key.setter
    def set_key(self, value):
        self.key = value
