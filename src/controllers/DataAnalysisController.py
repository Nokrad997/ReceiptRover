from src.services.DataAnalysisService import DataAnalysisService


class DataAnalysisController:
    def __init__(self):
        self.service = DataAnalysisService()

    # jeszcze nie zaimplementowane
    def getMounthlyStatement(self, receipts, year, month):
        """
        Generates a chart base on Monthly expenses
        Args:
            receipts: The receipt to be analysed.
            year: The year
            month: The month
        Returns:
            str: path to the chart
        """
        return self.service.getMounthlyStatement(receipts, year, month)

    def getShopStatement(self, receipts, year, month):
        """
        Generates a chart base on expensys from particular shops in selected month
        Args:
            receipts: The receipt to be analysed.
            year: The year
            month: The month
        Returns:
            str: path to the chart
        """
        return self.service.getShopStatement(receipts, year, month)

    def clearCharts(self):
        """
        Clear folder where charts are stored

        """
        self.service.clearCharts()
