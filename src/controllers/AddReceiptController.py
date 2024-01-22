import json
import tkinter as tk

from datetime import datetime
from ttkbootstrap import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

from src.controllers.ApiController import ApiController
from src.controllers.ScannerController import ScannerController
from src.views.View import View


"""
    This class is responsible for controlling the AddReceiptView.
    It is responsible for handling the user input and displaying the data.
    
    Attributes:
        addReceiptView (View): The view that is controlled by this controller.
        image (Image): The image that is displayed on the view.
        
    Methods:
        openDialog: Opens a file dialog and displays the image on the view.
        addProduct: Adds a products entry to the view for user to manual write.
        addProductFromList: Adds a product from the json list to the view.
"""


class AddReceiptController:
    def __init__(self, addReceiptView: View):
        self.addReceiptView = addReceiptView
        self.image = None

    """
        Opens a file dialog and takes the image path.

        Returns:
            str: The path to the image.
    """

    def openDialog(self) -> str:
        path = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(
                ("Image files", ("*.jpg", "*.jpeg", "*.png")),
                ("all files", "*.*"),
            ),
        )

        return path

    """
        Adds a products entry to the view for manual write by user.
    """

    def takeImageFromUser(self) -> None:
        path = self.openDialog()
        print(path)

        scannerController = ScannerController(path)
        scannerController.scan()
        pathForApi = scannerController.saveScanned(f"scanned_{datetime.now()}.jpg")

        self.image = Image.open(fp=pathForApi, mode="r")
        # self.addReceiptView.hideFrame()
        # self.addReceiptView.showImage(self.image)

        self.addProductFromList(pathForApi)

    """
        Method to adding new entrys for user to manual write.
    """

    def addProduct(self) -> None:
        try:
            childrensLength = len(self.addReceiptView.scrollableList.children)
            pixelsToAdd = 50 * (childrensLength // 3)
            
            self.addReceiptView.scrollableList.configure(height=pixelsToAdd + 50)

            entry = ttk.Entry(self.addReceiptView.scrollableList)
            count = ttk.Entry(self.addReceiptView.scrollableList)
            price = ttk.Entry(self.addReceiptView.scrollableList)

        except tk.TclError as e:
            print(f"An error occurred during widget creation: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        else:
            entry.place(x=10, y=pixelsToAdd, width=180, height=40)
            count.place(x=200, y=pixelsToAdd, width=45, height=40)
            price.place(x=255, y=pixelsToAdd, width=45, height=40)

    """
        Adds a product from the json list to the view.
    """

    def addProductFromList(self, path: str):
        apiController = ApiController()
        result = apiController.getReceiptData(path)
        print(result)
        shopName = result["shop"]
        print(shopName)
        self.addReceiptView.shopNameEntry.delete(0, tk.END)
        self.addReceiptView.shopNameEntry.insert(0, shopName)

        self.addReceiptView.hideFirstLine()

        products = result["products"]
        productsCount = len(products)

        self.addReceiptView.scrollableList.configure(height=productsCount * 50)
        
        for number, product in enumerate(products):
            productName = ttk.Entry(self.addReceiptView.scrollableList)
            productCount = ttk.Entry(self.addReceiptView.scrollableList)
            productPrice = ttk.Entry(self.addReceiptView.scrollableList)

            productName.insert(0, product[0])
            productCount.insert(0, f"{product[1]} szt.")
            productPrice.insert(0, f"{product[2]} zł")

            productName.place(x=10, y=50 * number, width=180, height=40)
            productCount.place(x=200, y=50 * number, width=45, height=40)
            productPrice.place(x=255, y=50 * number, width=45, height=40)

