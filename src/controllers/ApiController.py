from src.services.ApiService import ApiService


class ApiController:
    def __init__(self):
        self.apiService = ApiService()

    def getReceiptData(self, filePath):
        """
        Retrieves receipt data from the API by sending a POST request with the given file path.

        Args:
            filePath (str): The path to the receipt file.

        Returns:
            dict: The receipt data returned by the API.
        """
        result = self.apiService.post(filePath)
        return result
