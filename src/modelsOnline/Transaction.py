from datetime import datetime
from pydantic import BaseModel
from typing import Self


class Transaction(BaseModel):
    transactionsId: int
    userId: int
    date: datetime
    scanId: int
    key: str

    @property
    def getTransactionsId(self) -> int:
        return self.transactionsId

    @property
    def getUserId(self) -> int:
        return self.userId

    @property
    def getDate(self) -> datetime:
        return self.date

    @property
    def getScanId(self) -> int:
        return self.scanId

    @property
    def getKey(self) -> str:
        return self.key

    @getTransactionsId.setter
    def setTransactionsId(self, value: int):
        self.transactionsId = value

    @getUserId.setter
    def setUserId(self, value: int):
        self.userId = value

    @getDate.setter
    def setDate(self, value: datetime):
        self.date = value

    @getScanId.setter
    def setScanId(self, value: int):
        self.scanId = value

    @getKey.setter
    def setKey(self, value: str):
        self.key = value
