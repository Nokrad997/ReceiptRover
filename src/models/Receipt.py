class Receipt:
    def __init__(self, receipt_id, key, receipt_data):
        self.receipt_id = receipt_id
        self.key = key
        self.receipt_data = receipt_data

    @property
    def get_receipt_id(self):
        return self.receipt_id

    @property
    def get_key(self):
        return self.key

    @property
    def get_receipt_data(self):
        return self.receipt_data

    @get_receipt_id.setter
    def set_receipt_id(self, value):
        self.receipt_id = value

    @get_key.setter
    def set_key(self, value):
        self.key = value

    @get_receipt_data.setter
    def set_receipt_data(self, value):
        self.receipt_data = value
