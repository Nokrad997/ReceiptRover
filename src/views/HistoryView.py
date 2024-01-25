import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.scrolled import ScrolledFrame

from src.Navigator import Navigator

from src.controllers.AppController import AppController

from src.views.View import View


class HistoryView(View):
    """A class representing the HistoryView in the ReceiptRover application."""

    def __init__(self, canvas):
        """
        Initialize the HistoryView.

        Args:
            canvas (tk.Canvas): The canvas on which the view will be placed.
        """
        super().__init__(canvas)
        self.fontDict = {"small": ("Helvetica", 12), "medium": ("Helvetica", 16), "large": ("Helvetica", 20)}

        self.historyLabel = ttk.Label(self.canvas, font=self.fontDict['medium'], text="History")

        self.monthLabel = ttk.Label(self.canvas, text="Month")
        self.monthLabel.configure(justify=tk.CENTER)

        self.scrollableFrame = ScrolledFrame(self.canvas)
        self.fillScrollableFrame()

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        """Place the HistoryView on the canvas."""
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.historyLabel.place(x=10, y=10, width=300, height=40)

        self.scrollableFrame.place(x=0, y=50, width=320, height=590)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        """Hide the HistoryView."""
        self.historyLabel.place_forget()

        self.scrollableFrame.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()

    def fillScrollableFrame(self):
        """
        Fill the scrollable frame with the receipts.
        """
        appController = AppController()
        receipts, dates = appController.getHistory()
        # print(receipts, dates)
        combined_list = list(zip(receipts, dates))
        # print(combined_list)

        for receipt, date in combined_list:
            receiptFrame = ttk.Labelframe(self.scrollableFrame)
            receiptFrame.configure(bootstyle="default")

            dateLabel = ttk.Label(receiptFrame, text=date.strftime("%d/%m/%Y"))
            dateLabel.configure(font=self.fontDict['small'], justify=tk.LEFT)

            receiptLabel = ttk.Label(receiptFrame, text=receipt.shop)
            receiptLabel.configure(font=self.fontDict['small'], justify=tk.LEFT)

            receiptFrame.pack(expand=True, fill=tk.X, padx=15, pady=1, ipadx=5, ipady=2)
            dateLabel.pack(side=tk.LEFT)
            receiptLabel.pack(side=tk.RIGHT)