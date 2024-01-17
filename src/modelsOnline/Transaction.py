from datetime import datetime
from pydantic import BaseModel
from datetime import date
from typing import Self

class Transaction(BaseModel):
    transactions_id: int
    user_id: int
    date: datetime
    scan_id: int
    key: str
        
    def __init__(self, transactions_id : int = 0, user_id : int = 0, date : str = "", scan_id : int = 0, key : str = ''):
        super().__init__()
        self.transactions_id = transactions_id
        self.user_id = user_id
        self.date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') if date != "" else datetime.now()
        self.scan_id = scan_id
        self.key = key
        self.receipt= None
        
    @property
    def get_transactions_id(self) -> int:
        return self.transactions_id
    
    @property
    def get_user_id(self) -> int:
        return self.user_id
    
    @property
    def get_date(self) -> datetime:
        return self.date
    
    @property
    def get_scan_id(self) -> int:
        return self.scan_id
    
    @property
    def get_key(self) -> str:
        return self.key


    @get_transactions_id.setter
    def set_transactions_id(self, value : int):
        self.transactions_id = value

    @get_user_id.setter
    def set_user_id(self, value : int):
        self.user_id = value

    @get_date.setter
    def set_date(self, value : datetime):
        self.date = value

    @get_scan_id.setter
    def set_scan_id(self, value : int):
        self.scan_id = value

    @get_key.setter
    def set_key(self, value : str):
        self.key = value
    