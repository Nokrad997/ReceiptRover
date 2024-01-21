import tkinter as tk
import ttkbootstrap as ttk

from src.views.AddReceiptView import AddReceiptView
from src.Navigator import Navigator
from src.views.View import View
from src.views.AnalyseView import AnalyseView
from src.views.AddReceiptView import AddReceiptView
from src.views.LoginView import LoginView


class MainView(View):
    def __init__(self, canvas, root):
        super().__init__(canvas)
        self.root = root
        self.navbar = []

        # self.historyButton = ttk.Button(self.localCanvas, text="History")
        # self.historyButton.configure(bootstyle="outline")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.analyseButton = ttk.Button(self.navbarFrame, text="Analyse")
        self.analyseButton.configure(
            bootstyle="outline",
            command=lambda: Navigator().navigateTo(AnalyseView(self.canvas)),
        )

        self.addReceiptButton = ttk.Button(self.navbarFrame, text="Add receipt")
        self.addReceiptButton.configure(
            bootstyle="outline",
            command=lambda: Navigator().navigateTo(AddReceiptView(self.canvas)),
        )

        self.accountButton = ttk.Button(self.navbarFrame, text="Login")
        self.accountButton.configure(
            bootstyle="outline",
            command=lambda: Navigator().navigateTo(
                LoginView(self.canvas, "email", "password")
            ),
        )

        self.quitButton = ttk.Button(self.navbarFrame, text="Quit")
        self.quitButton.configure(bootstyle="outline", command=lambda: self.root.quit())

    def place(self):
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.navbarFrame.place(x=0, y=500, width=320, height=200)

        self.analyseButton.place(x=10, y=0, width=300, height=40)
        self.addReceiptButton.place(x=10, y=50, width=300, height=40)
        self.accountButton.place(x=10, y=100, width=300, height=40)
        self.quitButton.place(x=10, y=150, width=300, height=40)

    def hide(self):
        # self.canvas.place_forget()

        self.navbarFrame.place_forget()

        self.analyseButton.place_forget()
        self.addReceiptButton.place_forget()
        self.accountButton.place_forget()
        self.quitButton.place_forget()
