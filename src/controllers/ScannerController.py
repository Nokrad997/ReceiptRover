from src.services.ScannerService import ScannerService

class ScannerController:
    def __init__(self, filePath):
        self.scannerService = ScannerService(filePath)
        
    def scan(self):
        self.scannerService.scan()
        
    def saveScanned(self, filename, filePath = "scanned/") -> str:
        filePath = filePath + filename
        return self.scannerService.saveScanned(filePath)
