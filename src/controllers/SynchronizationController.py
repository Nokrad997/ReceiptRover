from src.services.SynchronizationService import SynchronizationService

class SynchronizationController:
    def __init__(self):
        self.synchronizationService = SynchronizationService()

    def synchronizeData(self, userId: int):
        if self.synchronizationService.checkData(userId):
            self.synchronizationService.synchronizeLocal()
            self.synchronizationService.synchronize_database()
