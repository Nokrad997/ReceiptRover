from src.Services.ApiService import ApiService

class ApiController:
    def __init__(self):
        self.apiService = ApiService()
        
    def getReceiptData(self, filePath):
        return self.apiService.post(filePath)
        
        
    