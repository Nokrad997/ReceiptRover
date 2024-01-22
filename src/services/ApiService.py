import requests
from src.exceptions.Exceptions import InvalidApiException
from src.repositories.ProductOfflineRepository import ProductOfflineRepository
from src.repositories.ReceiptOfflineRepository import ReceiptOfflineRepository


class ApiService:
    def __init__(self, url="http://pythontess:5000"):
        """
        Initializes an instance of the ApiService class.

        Parameters:
        - url (str): The URL of the API server. Default is "http://pythontess:5000".
        """
        self.url = "http://pythontess:5000"

    def post(self, file_path):
        """
        Sends an image file to the API server for processing.

        Parameters:
        - file_path (str): The path to the image file.

        Returns:
        - dict: The response from the API server.
        """
        try:
            response = requests.post(self.url, files={"file": open(file_path, "rb")})
            response = response.json()
            return response
        except Exception as e:
            raise InvalidApiException(f"Error occurred while sending image to api: {e}")
