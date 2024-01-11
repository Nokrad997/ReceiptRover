class OCRScanController(DatabaseController):
    def create_ocr_scan(self, scanned_image_data):
        query = "INSERT INTO ocr_scans (scanned_image_data) VALUES (%s);"
        data = (scanned_image_data,)
        return self.execute_query(query, data)
    
    