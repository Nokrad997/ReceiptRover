import tkinter as tk
import ttkbootstrap as ttk

from src.Navigator import Navigator
from src.views.View import View
from src.views.LoginView import LoginView
from src.views.AddReceiptView import AddReceiptView

class MainView(View):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.navbar = []

        # self.historyButton = ttk.Button(self.localCanvas, text="History")
        # self.historyButton.configure(bootstyle="outline")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.analyseButton = ttk.Button(self.navbarFrame, text="Analyse")
        self.analyseButton.configure(bootstyle="outline")

        self.addReceiptButton = ttk.Button(self.navbarFrame, text="Add receipt", command=lambda: Navigator().navigateTo(AddReceiptView(self.canvas)))
        self.addReceiptButton.configure(bootstyle="outline")
        
        self.accountButton = ttk.Button(self.navbarFrame, text="Login")
        self.accountButton.configure(bootstyle="outline", command=lambda: Navigator().navigateTo(LoginView(self.canvas, "email", "password")))



    def place(self):
        self.canvas.place(x=0, y=0, width=321, height=694)

        self.navbarFrame.place(x=0, y=624, width=321, height=50)

        self.analyseButton.place(x=3.5, y=10, width=100, height=40)
        self.addReceiptButton.place(x=110.5, y=10, width=100, height=40)
        self.accountButton.place(x=217.5, y=10, width=100, height=40)

    def hide(self):
        # self.canvas.place_forget()

        self.navbarFrame.place_forget()

        self.analyseButton.place_forget()
        self.addReceiptButton.place_forget()
        self.accountButton.place_forget()