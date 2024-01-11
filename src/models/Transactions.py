from src.models.Model import Model
from src.models.Receipt import Receipt

from pydantic import BaseModel
from datetime import date
from typing import Self

class Transactions(Model, BaseModel):
    transactions_id: int
    user_id: int
    date: date
    scan_id: int
    key: str
    receipt: Receipt
        
    def __init__(self, transactions_id : int = 0, user_id : int = 0, date : date = 0, scan_id : int = 0, key : str = ''):
        super().__init__()

        self.transactions_id = transactions_id
        self.user_id = user_id
        self.date = date
        self.scan_id = scan_id
        self.key = key
        self.receipt= None
        
    def addTransaction(self) -> list:
        return self.executeQuery(f'INSERT INTO "Transactions" (user_id, date, scan_id, key) VALUES (\'{self.user_id}\', \'{self.date}\', \'{self.scan_id}\', \'{self.key}\') RETURNING *')
    
    def getTransactions(self) -> list:
        return self.executeQuery('SELECT * FROM "Transactions"')
    
    def getTransactionById(self, id) -> Self:
        res = self.executeQuery(f'SELECT * FROM "Transactions" WHERE transactions_id = \'{id}\'')
        
        if(res):
            return Transactions(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5])
        else:
            return res
    
    def getTransactionsByUserId(self, id) -> list[Self]:
        res = self.executeQuery(f'SELECT * FROM "Transactions" WHERE user_id = \'{id}\'')
        
        if(res):
            for i in range(len(res)):
                res[i] = Transactions(res[i][0], res[i][1], res[i][2], res[i][3], res[i][4], res[i][5])
            return res
        else:
            return res
        
    def getTransactionsByDate(self, date) -> list[Self]:
        res = self.executeQuery(f'SELECT * FROM "Transactions" WHERE date = \'{date}\'')
        
        if(res):
            for i in range(len(res)):
                res[i] = Transactions(res[i][0], res[i][1], res[i][2], res[i][3], res[i][4], res[i][5])
            return res
        else:
            return res
        
    