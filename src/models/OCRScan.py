from pydantic import BaseModel

class OCRScan(BaseModel):
    scan_id: int
    scanned_image_data: list[int]

    @property
    def get_scan_id(self):
        return self.scan_id

    @property
    def get_scanned_image_data(self):
        return self.scanned_image_data

    @get_scan_id.setter
    def set_scan_id(self, value):
        self.scan_id = value

    @get_scanned_image_data.setter
    def set_scanned_image_data(self, value):
        self.scanned_image_data = value