from pydantic import BaseModel


class OCRScan(BaseModel):
    """
    Represents an OCR scan with scan ID and scanned image data.
    """

    scanId: int
    scannedImageData: list[int]

    @property
    def getScanId(self):
        """
        Get the scan ID.

        Returns:
            int: The scan ID.
        """
        return self.scanId

    @property
    def getScannedImageData(self):
        """
        Get the scanned image data.

        Returns:
            list[int]: The scanned image data.
        """
        return self.scannedImageData

    @getScanId.setter
    def setScanId(self, value):
        """
        Set the scan ID.

        Args:
            value (int): The scan ID to set.
        """
        self.scanId = value

    @getScannedImageData.setter
    def setScannedImageData(self, value):
        """
        Set the scanned image data.

        Args:
            value (list[int]): The scanned image data to set.
        """
        self.scannedImageData = value
