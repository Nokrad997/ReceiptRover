from src.services.ScannerService import ScannerService


class ScannerController:
    def __init__(self, filePath):
        """
        Initializes a ScannerController object.

        Parameters:
        - filePath (str): The file path to be used by the ScannerService.

        Returns:
        None
        """
        self.scannerService = ScannerService(filePath)

    def scan(self):
        """
        Calls the scan method of the ScannerService.

        Parameters:
        None

        Returns:
        None
        """
        self.scannerService.scan()

    def saveScanned(self, filename, filePath="scanned/") -> str:
        """
        Saves the scanned file with the given filename and file path.

        Parameters:
        - filename (str): The name of the file to be saved.
        - filePath (str): The file path where the file should be saved. Default is "scanned/".

        Returns:
        str: The file path where the file was saved.
        """
        filePath = filePath + filename
        return self.scannerService.saveScanned(filePath)
