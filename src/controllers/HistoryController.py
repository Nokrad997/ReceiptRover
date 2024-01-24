from src.services.HistoryService import HistoryService

class HistoryController:
    def __init__(self):
        self.historyService = HistoryService()
    
    def getHistory(self):
        """
        Gets the history from the data provider.

        Returns:
            list: A list of receipts.
            list: A list of dates.
        """
        return self.historyService.getHistory()