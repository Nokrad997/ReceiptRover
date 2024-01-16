from pydantic import BaseModel
from typing import Self

class Receipt(BaseModel):
    receipt_id: int
    key: str
    receipt: str
    
    @property
    def get_receipt_id(self) -> int:
        return self.receipt_id
    
    @property
    def get_key(self) -> str:
        return self.key
    
    
    @get_receipt_id.setter
    def set_receipt_id(self, value : int):
        self.receipt_id = value
    
    @get_key.setter
    def set_key(self, value : str):
        self.key = value



    
        
        
    
