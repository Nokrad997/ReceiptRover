from src.services.SynchronizationService import SynchronizationService


class SynchronizationController:
    def __init__(self):
        self.synchronizationService = SynchronizationService()

    def synchronizeData(self, userId: int):
        """
        Synchronizes data for a given user.

        Args:
            userId (int): The ID of the user.

        Returns:
            None
        """
        if self.synchronizationService.checkData(userId):
            self.synchronizationService.synchronizeLocal()
            self.synchronizationService.synchronize_database()
