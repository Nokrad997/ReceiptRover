from datetime import datetime
from pydantic import BaseModel
from datetime import date
from typing import Self, Optional

class Transaction(BaseModel):
    transactions_id: int
    user_id: int
    date: datetime
    scan_id: Optional[int]
    key: str
        
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
    