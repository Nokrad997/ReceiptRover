from src.repositories.Repository import Repository


class OCRScanController(Repository):
    def createOcrScan(self, scannedImageData):
        query = (
            f"INSERT INTO ocr_scans (scanned_image_data) VALUES ({scannedImageData});"
        )
        return self.executeQuery(query)

    def getOcrScanById(self, scanId):
        query = f"SELECT * FROM ocr_scans WHERE scan_id = {scanId};"
        return self.executeQuery(query)

    def updateOcrScanData(self, scanId, newScannedImageData):
        query = f"UPDATE ocr_scans SET scanned_image_data = {newScannedImageData} WHERE scan_id = {scanId};"
        return self.executeQuery(query)

    def deleteOcrScan(self, scanId):
        query = f"DELETE FROM ocr_scans WHERE scan_id = {scanId};"
        return self.executeQuery(query)
