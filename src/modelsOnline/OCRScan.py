from pydantic import BaseModel

class OCRScan(BaseModel):
    scanId: int
    scannedImageData: list[int]

    @property
    def getScanId(self):
        return self.scanId

    @property
    def getScannedImageData(self):
        return self.scannedImageData

    @getScanId.setter
    def setScanId(self, value):
        self.scanId = value

    @getScannedImageData.setter
    def setScannedImageData(self, value):
        self.scannedImageData = value
