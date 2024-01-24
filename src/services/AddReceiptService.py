import json
import tkinter as tk

from datetime import datetime
from ttkbootstrap import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

from src.controllers.ApiController import ApiController
from src.controllers.ScannerController import ScannerController
from src.views.View import View

class AddReceiptService:
    def __init__(self, addReceiptView : View):
        """
        Initialize the AddReceiptService class.

        Parameters:
        - addReceiptView (View): The view object for adding receipts.
        """
        self.addReceiptView = addReceiptView
        self.scroll = self.addReceiptView.scrollableList
        self.image = None
        
    def openDialog(self) -> str:
        """
        Open a file dialog to select a file.

        Returns:
        - str: The path of the selected file.
        """
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
    
    def processImage(self, path: str) -> str:
        """
        Process the selected image.

        Parameters:
        - path (str): The path of the selected image.

        Returns:
        - str: The path of the processed image.
        """
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
    
    def addProduct(self) -> None:
        """
        Add a product to the receipt.

        Raises:
        - tk.TclError: If an error occurs during widget creation.
        - Exception: If an unexpected error occurs.
        """
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
            
    def iamgeToJSON(self, path: str) -> dict:
        """
        Convert an image to JSON.

        Parameters:
        - path (str): The path of the image.

        Returns:
        - dict: The JSON data extracted from the image.
        """
        apiController = ApiController()
        result = apiController.getReceiptData(path)
        print(result)
        return result
    
    def addProductFromList(self, json: dict) -> None:
        """
        Add products from a JSON object to the receipt.

        Parameters:
        - json (dict): The JSON object containing the product data.
        """
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
            
    def addReceiptController(self) -> None:
        """
        Controller for adding a receipt.

        - Opens a file dialog to select a file.
        - Processes the selected file (image or JSON).
        - Adds the products to the receipt.
        """
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
