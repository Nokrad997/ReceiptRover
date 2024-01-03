import Model
from pydantic import BaseModel
from typing import Self

class OCRScan(Model, BaseModel):
    id: int
    scanned_immage: bytes
    def __init__(self, id : int = 0, scanned_immage : bytes = b''):
        super().__init__()
        self.id = id
        self.scanned_immage = scanned_immage
        
    def addScan(self) -> list:
        return self.executeQuery(f'INSERT INTO "OCRScan" (scanned_immage) VALUES (\'{self.scanned_immage}\') RETURNING *')
    
    def getScans(self) -> list[Self]:
        res = self.executeQuery('SELECT * FROM "OCRScan"')
        if (res):
            for i in range(len(res)):
                res[i] = OCRScan(res[i][0], res[i][1])
            return res
        else:
            return res
        
    def getScanById(self, id) -> Self:
        res = self.executeQuery(f'SELECT * FROM "OCRScan" WHERE id = \'{id}\'')
        
        if(res):
            return OCRScan(res[0][0], res[0][1])
        else:
            return res
        
    