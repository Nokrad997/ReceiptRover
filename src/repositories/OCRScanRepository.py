from src.repositories.Repository import Repository


class OCRScanController(Repository):
    def createOcrScan(self, scannedImageData):
        """
        Creates a new OCR scan record in the database.

        Args:
            scannedImageData (str): The scanned image data.

        Returns:
            int: The ID of the newly created OCR scan record.
        """
        query = (
            f'INSERT INTO ocr_scans (scanned_image_data) VALUES ("{scannedImageData}");'
        )
        return self.executeQuery(query)

    def getOcrScanById(self, scanId):
        """
        Retrieves an OCR scan record from the database by its ID.

        Args:
            scanId (int): The ID of the OCR scan record.

        Returns:
            dict: The OCR scan record.
        """
        query = f"SELECT * FROM ocr_scans WHERE scan_id = {scanId};"
        return self.executeQuery(query)

    def updateOcrScanData(self, scanId, newScannedImageData):
        """
        Updates the scanned image data of an existing OCR scan record in the database.

        Args:
            scanId (int): The ID of the OCR scan record.
            newScannedImageData (str): The new scanned image data.

        Returns:
            int: The number of affected rows in the database.
        """
        query = f'UPDATE ocr_scans SET scanned_image_data = "{newScannedImageData}" WHERE scan_id = {scanId};'
        return self.executeQuery(query)

    def deleteOcrScan(self, scanId):
        """
        Deletes an OCR scan record from the database by its ID.

        Args:
            scanId (int): The ID of the OCR scan record.

        Returns:
            int: The number of affected rows in the database.
        """
        query = f"DELETE FROM ocr_scans WHERE scan_id = {scanId};"
        return self.executeQuery(query)
