import os
import tkinter as tk
from ttkbootstrap import ttk

from src.Navigator import Navigator
from src.views.View import View
class AddReceiptView(View):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.currentPath = os.getcwd()
        # print(self.currentPath)
        self.tkImageReference = None

        self.addReceiptLabel = ttk.Label(self.canvas, text="Add Receipt")
        self.addReceiptLabel.configure(bootstyle="primary")

        self.addReceiptButton = ttk.Button(self.canvas, text="Add Receipt", command=lambda: self.openDialog()) 
        self.addReceiptButton.configure(bootstyle="primary")

        self.pathLabel = ttk.Label(self.canvas, text="Path")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(bootstyle="outline", command=lambda: Navigator().navigateBack())

    def place(self):
        self.canvas.place(x=0, y=0, width=321, height=694)
        
        self.addReceiptLabel.place(x=60, y=145, width=200, height=20)
        self.addReceiptButton.place(x=60, y=165, width=200, height=30)

        self.navbarFrame.place(x=0, y=624, width=321, height=50)

    def hide(self):
        self.addReceiptLabel.place_forget()
        self.addReceiptButton.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()

    def openDialog(self):
        pass