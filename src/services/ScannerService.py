from src.scannerModule.Scanner import Scanner

class ScannerService:
    def __init__(self, filePath):
        self.scanner = Scanner(filePath)
        
    def scan(self):
        self.scanner.scan()
        
    def saveScanned(self, filePath):
        return self.scanner.saveScanned(filePath)