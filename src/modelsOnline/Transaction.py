from datetime import datetime
from pydantic import BaseModel
from typing import Self


class Transaction(BaseModel):
    """
    Represents a transaction.

    Attributes:
        transactionsId (int): The ID of the transaction.
        userId (int): The ID of the user associated with the transaction.
        date (datetime): The date of the transaction.
        scanId (int): The ID of the scan associated with the transaction.
        key (str): The key associated with the transaction.

    Methods:
        getTransactionsId() -> int: Returns the ID of the transaction.
        getUserId() -> int: Returns the ID of the user associated with the transaction.
        getDate() -> datetime: Returns the date of the transaction.
        getScanId() -> int: Returns the ID of the scan associated with the transaction.
        getKey() -> str: Returns the key associated with the transaction.
        setTransactionsId(value: int): Sets the ID of the transaction.
        setUserId(value: int): Sets the ID of the user associated with the transaction.
        setDate(value: datetime): Sets the date of the transaction.
        setScanId(value: int): Sets the ID of the scan associated with the transaction.
        setKey(value: str): Sets the key associated with the transaction.
    """

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
