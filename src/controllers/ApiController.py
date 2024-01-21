from src.services.ApiService import ApiService

class ApiController:
    def __init__(self):
        self.apiService = ApiService()
        
    def getReceiptData(self, filePath):
        result = self.apiService.post(filePath)
        return result
        
        
    