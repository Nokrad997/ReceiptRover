import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.scrolled import ScrolledFrame

from src.Navigator import Navigator

from src.views.View import View


class ReceiptView(View):
    """A class representing the ReceiptView in the ReceiptRover application."""

    def __init__(self, canvas, receipt):
        """
        Initialize the ReceiptView.

        Args:
            canvas (tk.Canvas): The canvas on which the view will be placed.
        """
        super().__init__(canvas)
        self.fontDict = {"small": ("Helvetica", 12), "medium": ("Helvetica", 16), "large": ("Helvetica", 20)}

        self.receipt = receipt

        self.shopLabel = ttk.Label(self.canvas, font=self.fontDict['medium'], text=self.receipt.shop)

        self.productLabel = ttk.Label(self.canvas, text="Product")
        self.productLabel.configure(font=self.fontDict["small"], justify=tk.CENTER)

        self.countLabel = ttk.Label(self.canvas, text="Count")
        self.countLabel.configure(font=self.fontDict["small"], justify=tk.CENTER)

        self.priceLabel = ttk.Label(self.canvas, text="Price")
        self.priceLabel.configure(font=self.fontDict["small"], justify=tk.CENTER)

        self.scrollableFrame = ScrolledFrame(self.canvas)
        self.fillScrollableFrame()

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        """Place the ReceiptView on the canvas."""
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.shopLabel.place(x=10, y=10, width=300, height=40)

        self.productLabel.place(x=10, y=50, width=145, height=40)
        self.countLabel.place(x=165, y=50, width=50, height=40)
        self.priceLabel.place(x=225, y=50, width=70, height=40)

        self.scrollableFrame.place(x=0, y=100, width=320, height=540)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        """Hide the ReceiptView."""
        self.shopLabel.place_forget()

        self.productLabel.place_forget()
        self.countLabel.place_forget()
        self.priceLabel.place_forget()

        self.scrollableFrame.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()

    def fillScrollableFrame(self):
        """
        Fill the scrollable frame with the receipts.
        """
        for number, product in enumerate(self.receipt.products):
            print(product)

            productName = ttk.Entry(self.scrollableFrame)
            productName.insert(0, product.name)
            productName.configure(font=self.fontDict["small"], justify=tk.LEFT, state="readonly")

            productCount = ttk.Entry(self.scrollableFrame)
            productCount.insert(0, product.quantity)
            productCount.configure(font=self.fontDict["small"], justify=tk.CENTER, state="readonly")

            productPrice = ttk.Entry(self.scrollableFrame)
            productPrice.insert(0, product.price)
            productPrice.configure(font=self.fontDict["small"], justify=tk.CENTER, state="readonly")

            productName.place(x=10, y=50 * number + 1, width=145, height=40)
            productCount.place(x=165, y=50 * number + 1, width=50, height=40)
            productPrice.place(x=225, y=50 * number + 1, width=70, height=40)
