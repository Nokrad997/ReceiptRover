from src.scannerModule.Scanner import Scanner


class ScannerService:
    def __init__(self, filePath):
        """
        Initializes the ScannerService with the given file path.

        Args:
            filePath (str): The path to the file to be scanned.
        """
        self.scanner = Scanner(filePath)

    def scan(self):
        """
        Initiates the scanning process using the Scanner object.
        """
        self.scanner.scan()

    def saveScanned(self, filePath):
        """
        Saves the scanned document to the specified file path.

        Args:
            filePath (str): The path where the scanned document should be saved.

        Returns:
            bool: True if the document was successfully saved, False otherwise.
        """
        return self.scanner.saveScanned(filePath)
