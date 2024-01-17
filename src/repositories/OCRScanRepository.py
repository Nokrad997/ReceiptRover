from repositories.DatabaseRepository import DatabaseRepository

class OCRScanController(DatabaseController):
    def createOcrScan(self, scanned_image_data):
        query = f"INSERT INTO ocr_scans (scanned_image_data) VALUES ({scanned_image_data});"
        return self.executeQuery(query)

    def getOcrScanById(self, scan_id):
        query = f"SELECT * FROM ocr_scans WHERE scan_id = {scan_id};"
        data = (scan_id)
        return self.executeQuery(query)

    def updateOcrScanData(self, scan_id, new_scanned_image_data):
        query = f"UPDATE ocr_scans SET scanned_image_data = {new_scanned_image_data} WHERE scan_id = {scan_id};"
        return self.executeQuery(query)

    def deleteOcrScan(self, scan_id):
        query = f"DELETE FROM ocr_scans WHERE scan_id = {scan_id};"
        return self.executeQuery(query)
    