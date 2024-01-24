from src.services.DataAnalysisService import DataAnalysisService
class DataAnalysisController():
    def __init__(self):
        self.service = DataAnalysisService()
    
    def getMounthlyStatement(self,receipt,year,month):
        """
        Generates a chart base on Monthly expenses
        Args:
            receipt: The receipt to be analysed.
            year: The year
            month: The month
        Returns:
            str: path to the chart
        """
        return self.service.getMounthlyStatement(receipt,year,month)
        
    def getShopStatement(self,receipt,year,month):
        """
        Generates a chart base on expensys from particular shops
        Args:
            receipt: The receipt to be analysed.
            year: The year
            month: The month
        Returns:
            str: path to the chart
        """
        return self.service.getShopStatement(receipt,year,month)
    
    def clearCharts(self):
        """
        Clear folder where charts are stored
        
        """
        self.service.clearCharts()