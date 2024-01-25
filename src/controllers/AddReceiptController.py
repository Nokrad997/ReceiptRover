from src.services.AddReceiptService import AddReceiptService
from src.views.View import View


class AddReceiptController:
    def __init__(self, addReceiptView: View):
        """
        Initializes an instance of AddReceiptController.

        Args:
            addReceiptView (View): The view object used for displaying the add receipt dialog.
        """
        self.addReceiptService = AddReceiptService(addReceiptView)

    def openDialog(self) -> str:
        """
        Opens the add receipt dialog.

        Returns:
            str: The result of opening the dialog.
        """
        self.addReceiptService.openDialog()

    def processImage(self, path: str) -> str:
        """
        Processes the image at the specified path.

        Args:
            path (str): The path to the image file.

        Returns:
            str: The result of processing the image.
        """
        self.addReceiptService.processImage(path)

    def addProduct(self) -> None:
        """
        Adds input to the frame so that the user can manually add a product to the list.
        """
        self.addReceiptService.addProduct()

    def iamgeToJSON(self, path: str) -> dict:
        """
        Converts the image at the specified path to JSON format.

        Args:
            path (str): The path to the image file.

        Returns:
            dict: The JSON representation of the image.
        """
        self.addReceiptService.iamgeToJSON(path)

    def addProductFromList(self, json: dict) -> None:
        """
        Adds a product to the receipt from a JSON representation.

        Args:
            json (dict): The JSON representation of the product.
        """
        self.addReceiptService.addProductFromList(json)

    def addReceiptController(self) -> None:
        """
        Adds the receipt to the view.
        """
        return self.addReceiptService.addReceiptController()
    
    # def saveReceipt(self, resultList: list) -> None:
    #     """
    #     Saves the receipt.

    #     Args:
    #         resultList (list): The list of products.
    #     """
    #     self.addReceiptService.saveReceipt(resultList)
