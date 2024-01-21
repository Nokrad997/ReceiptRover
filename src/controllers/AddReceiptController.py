import json
import tkinter as tk

from ttkbootstrap import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

from src.controllers.ApiController import ApiController
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

        self.image = Image.open(fp=path, mode="r")
        self.addReceiptView.hideFrame()
        self.addReceiptView.showImage(self.image)

        self.addProductFromList(path)

    """
        Method to adding new entrys for user to manual write.
    """

    def addProduct(self) -> None:
        try:
            childrensLength = len(self.addReceiptView.scrollableList.children)
            pixelsToAdd = 50 * (childrensLength // 3)
            if pixelsToAdd > 6000:
                messagebox.showerror(
                    title="Error", message="Too many products on the receipt"
                )
                raise Exception("Too many products")

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
        pass
