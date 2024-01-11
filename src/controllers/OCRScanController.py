class OCRScanController(DatabaseController):
    def create_ocr_scan(self, scanned_image_data):
        query = "INSERT INTO ocr_scans (scanned_image_data) VALUES (%s);"
        data = (scanned_image_data,)
        return self.execute_query(query, data)

    def get_ocr_scan_by_id(self, scan_id):
        query = "SELECT * FROM ocr_scans WHERE scan_id = %s;"
        data = (scan_id,)
        return self.execute_query(query, data)

    def update_ocr_scan_data(self, scan_id, new_scanned_image_data):
        query = "UPDATE ocr_scans SET scanned_image_data = %s WHERE scan_id = %s;"
        data = (new_scanned_image_data, scan_id)
        return self.execute_query(query, data)

    def delete_ocr_scan(self, scan_id):
        query = "DELETE FROM ocr_scans WHERE scan_id = %s;"
        data = (scan_id,)
        return self.execute_query(query, data)
    