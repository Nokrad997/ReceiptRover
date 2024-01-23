import os
import tkinter as tk
from PIL import Image, ImageTk
from ttkbootstrap import ttk
from ttkbootstrap.scrolled import ScrolledFrame

from src.controllers.AppController import AppController

from src.Navigator import Navigator
from src.views.View import View


class AddReceiptView(View):
    """
    A class representing the view for adding a receipt.

    Attributes:
    - canvas: The canvas on which the view is placed.
    - currentPath: The current working directory path.
    - tkImageReference: A reference to the Tkinter image.
    - shopNameEntry: The entry widget for entering the shop name.
    - imageLabel: The label widget for displaying the image.
    - scrollableList: The scrolled frame widget for displaying the list of products.
    - firstEntry: The entry widget for entering the first product.
    - firstCount: The entry widget for entering the count of the first product.
    - firstPrice: The entry widget for entering the price of the first product.
    - addItemButton: The button for adding a product.
    - navbarFrame: The frame widget for the navigation bar.
    - navbarLabel: The label widget for displaying the navigation bar text.
    - cameraButton: The button for taking a photo of the receipt.
    - importImageButton: The button for importing an image of the receipt.
    - saveButton: The button for saving the receipt.
    - backButton: The button for navigating back.

    Methods:
    - place(): Places the view on the canvas.
    - hide(): Hides the view.
    - hideFirstLine(): Hides the first line of the product list.
    """

    def __init__(self, canvas):
        super().__init__(canvas)
        self.currentPath = os.getcwd()
        print(self.currentPath)
        self.tkImageReference = None

        self.shopNameEntry = ttk.Entry(self.canvas)
        self.shopNameEntry.insert(0, "shop name")
        self.shopNameEntry.bind(
            "<FocusIn>",
            lambda event: self.shopNameEntry.delete(0, tk.END)
            if self.shopNameEntry.get() == "shop name"
            else None,
        )
        self.shopNameEntry.bind(
            "<FocusOut>",
            lambda event: self.shopNameEntry.insert(0, "shop name")
            if self.shopNameEntry.get() == ""
            else None,
        )

        self.imageLabel = ttk.Label(self.canvas)

        self.scrollableList = ScrolledFrame(self.canvas)

        self.firstEntry = ttk.Entry(self.scrollableList)
        self.firstEntry.insert(0, "product")
        self.firstEntry.bind(
            "<FocusIn>",
            lambda event: self.firstEntry.delete(0, tk.END)
            if self.firstEntry.get() == "product"
            else None,
        )
        self.firstEntry.bind(
            "<FocusOut>",
            lambda event: self.firstEntry.insert(0, "product")
            if self.firstEntry.get() == ""
            else None,
        )

        self.firstCount = ttk.Entry(self.scrollableList)
        self.firstCount.insert(0, "count")
        self.firstCount.bind(
            "<FocusIn>",
            lambda event: self.firstCount.delete(0, tk.END)
            if self.firstCount.get() == "count"
            else None,
        )
        self.firstCount.bind(
            "<FocusOut>",
            lambda event: self.firstCount.insert(0, "count")
            if self.firstCount.get() == ""
            else None,
        )

        self.firstPrice = ttk.Entry(self.scrollableList)
        self.firstPrice.insert(0, "price")
        self.firstPrice.bind(
            "<FocusIn>",
            lambda event: self.firstPrice.delete(0, tk.END)
            if self.firstPrice.get() == "price"
            else None,
        )
        self.firstPrice.bind(
            "<FocusOut>",
            lambda event: self.firstPrice.insert(0, "price")
            if self.firstPrice.get() == ""
            else None,
        )

        self.addIcon = tk.PhotoImage(
            file=f"{self.currentPath}/src/icons/plus 30x30.png"
        )
        self.addItemButton = ttk.Button(
            self.canvas,
            compound=tk.TOP,
            image=self.addIcon,
            padding=3,
            command=lambda: AppController.addProduct(addReceiptView=self),
        )
        self.addItemButton.configure(bootstyle="outline")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.navbarLabel = ttk.Label(
            self.navbarFrame,
            text="Take photo of receipt or import image",
            anchor=tk.CENTER,
        )

        self.cameraIcon = tk.PhotoImage(
            file=f"{self.currentPath}/src/icons/camera 30x30.png"
        )
        self.cameraButton = ttk.Button(
            self.navbarFrame, compound=tk.TOP, image=self.cameraIcon, padding=3
        )
        self.cameraButton.configure(bootstyle="outline")

        self.imageIcon = tk.PhotoImage(
            file=f"{self.currentPath}/src/icons/image 30x30.png"
        )
        self.importImageButton = ttk.Button(
            self.navbarFrame, compound=tk.TOP, image=self.imageIcon, padding=3
        )
        self.importImageButton.configure(
            bootstyle="outline",
            command=lambda: AppController.addReceiptController(addReceiptView=self),
        )

        self.saveButton = ttk.Button(self.navbarFrame, text="Save")
        self.saveButton.configure(bootstyle="outline-success")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        """
        Places the view on the canvas.
        """
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.shopNameEntry.place(x=10, y=10, width=300, height=40)

        self.scrollableList.place(x=0, y=60, width=320, height=400)

        self.firstEntry.place(x=10, y=0, width=145, height=40)
        self.firstCount.place(x=165, y=0, width=50, height=40)
        self.firstPrice.place(x=225, y=0, width=70, height=40)

        self.addItemButton.place(x=270, y=470, width=40, height=40)

        self.navbarFrame.place(x=0, y=520, width=320, height=180)
        self.navbarLabel.place(x=0, y=0, width=320, height=20)

        self.cameraButton.place(x=10, y=30, width=145, height=40)
        self.importImageButton.place(x=165, y=30, width=145, height=40)
        self.saveButton.place(x=10, y=80, width=300, height=40)
        self.backButton.place(x=10, y=130, width=300, height=40)

    def hide(self):
        """
        Hides the view.
        """
        self.shopNameEntry.place_forget()

        self.imageLabel.place_forget()

        self.scrollableList.place_forget()

        self.addItemButton.place_forget()

        self.navbarFrame.place_forget()
        self.navbarLabel.place_forget()

        self.cameraButton.place_forget()
        self.importImageButton.place_forget()
        self.backButton.place_forget()

    def hideFirstLine(self):
        """
        Hides the first line of the product list.
        """
        self.firstEntry.place_forget()
        self.firstCount.place_forget()
        self.firstPrice.place_forget()
