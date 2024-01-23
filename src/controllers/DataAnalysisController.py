from src.services.DataAnalysisService import DataAnalysisService
class DataAnalysisController():
    def __init__(self):
        self.service = DataAnalysisService()
    
    def getMounthlyStatement(self,receipt):
        """
        Generates a chart base on Monthly expenses
        Args:
            receipt: The receipt to be analysed.
        Returns:
            str: path to the chart
        """
        return self.service.getMounthlyStatement(receipt)
        
    def getShopStatement(self,receipt):
        """
        Generates a chart base on expensys from particular shops
        Args:
            receipt: The receipt to be analysed.
        Returns:
            str: path to the chart
        """
        return self.service.getShopStatement(receipt)
    
    def clearCharts(self):
        """
        Clear folder where charts are stored
        
        """
        self.service.clearCharts()