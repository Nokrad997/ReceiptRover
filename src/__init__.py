from .modelsOnline import User, OCRScan, Product, Receipt, Transaction
from .controllers import RegistrationController, LoginController, DataController, SynchronizationController, ReceiptController
from .views import RegistrationView, LoginView, ProductView
from .repositories import Repository, UserRepository, OCRScanRepository, ReceiptRepository, TransactionRepository,ProductOfflineRepository,ReceiptOfflineRepository


# from .controllers import DataController

# from .repositories import Repository, ProductOfflineRepository,ReceiptOfflineRepository