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
        self.scroll = self.addReceiptView.scrollableList
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
                ("JSON files", "*.json"),
                ("all files", "*.*"),
            ),
        )

        return path

    """
        Adds a products entry to the view for manual write by user.
    """

    def processImage(self, path: str) -> str:
        scannerController = ScannerController(path)
        scannerController.scan()
        date = (
            str(datetime.now())
            .replace(" ", "_")
            .replace(":", "_")
            .replace(".", "_")
            .replace("-", "_")
        )
        messagebox.showinfo("Date", date)
        pathForApi = scannerController.saveScanned(f"scanned_{date}.jpg")
        messagebox.showinfo(
            "Info", f"Image processed successfully. Name: '{pathForApi}'"
        )

        return pathForApi

    """
        Method to adding new entrys for user to manual write.
    """

    def addProduct(self) -> None:
        try:
            childrensLength = len(self.scroll.children)
            pixelsToAdd = 50 * (childrensLength // 3)

            self.addReceiptView.scrollableList.configure(height=pixelsToAdd + 50)

            entry = ttk.Entry(self.scroll)
            count = ttk.Entry(self.scroll)
            price = ttk.Entry(self.scroll)

        except tk.TclError as e:
            print(f"An error occurred during widget creation: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        else:
            entry.place(x=10, y=pixelsToAdd, width=145, height=40)
            count.place(x=165, y=pixelsToAdd, width=50, height=40)
            price.place(x=225, y=pixelsToAdd, width=70, height=40)

    """
        Method to adding new entrys for user to manual write.
        
        Returns:
            dict: The json data from the api.
    """

    def iamgeToJSON(self, path: str) -> dict:
        apiController = ApiController()
        result = apiController.getReceiptData(path)
        print(result)
        return result

    """
        Adds a product from the json list to the view.
    """

    def addProductFromList(self, json: dict) -> None:
        shopName = json["shop"]
        print(shopName)
        for child in self.scroll.winfo_children():
            child.destroy()

        self.addReceiptView.shopNameEntry.delete(0, tk.END)
        self.addReceiptView.shopNameEntry.insert(0, shopName)

        products = json["products"]
        productsCount = len(products)

        self.scroll.configure(height=productsCount * 50)

        for number, product in enumerate(products):
            productName = ttk.Entry(self.scroll)
            productCount = ttk.Entry(self.scroll)
            productPrice = ttk.Entry(self.scroll)

            productName.insert(0, product[0])
            productCount.insert(0, f"{product[1]} szt.")
            productPrice.insert(0, f"{product[2]} zł")

            productName.place(x=10, y=50 * number, width=145, height=40)
            productCount.place(x=165, y=50 * number, width=50, height=40)
            productPrice.place(x=225, y=50 * number, width=70, height=40)

    """
        Method to control the view.
    """

    def addReceiptController(self) -> None:
        path = self.openDialog()

        if not path:
            return

        if path.endswith(".json"):
            self.addProductFromList(json.open(path))
        elif path.endswith((".jpg", ".jpeg", ".png")):
            pathForAPI = self.processImage(path)
            result = self.iamgeToJSON(pathForAPI)
            self.addProductFromList(result)
        else:
            messagebox.showerror("Error", "Invalid file format.")

        return
