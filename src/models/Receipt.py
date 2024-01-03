from src.models.Model import Model
from pydantic import BaseModel
from typing import Self

class Receipt(Model, BaseModel):
    receipt_id: int
    key: str
    receipt: bytes
    
    def __init__(self, receipt_id : int = 0, key : str = '', receipt : bytes = b''):
        super().__init__()
        self.receipt_id = receipt_id
        self.key = key
        self.receipt = receipt
    
    def addReceipt(self) -> list:
        return self.executeQuery(f'INSERT INTO "Receipt" (key, receipt) VALUES (\'{self.key}\', \'{self.receipt}\') RETURNING *')
    
    def getReceipts(self) -> list[Self]:
        res = self.executeQuery('SELECT * FROM "Receipt"')
        if (res):
            for i in range(len(res)):
                res[i] = Receipt(res[i][0], res[i][1], res[i][2])
            return res
        else:
            return res
        
    def getReceiptById(self, id) -> Self:
        res = self.executeQuery(f'SELECT * FROM "Receipt" WHERE receipt_id = \'{id}\'')
        
        if(res):
            return Receipt(res[0][0], res[0][1], res[0][2])
        else:
            return res
        
        
    
