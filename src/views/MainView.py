import os
import tkinter as tk
import ttkbootstrap as ttk

from src.views.AddReceiptView import AddReceiptView
from src.Navigator import Navigator

from src.controllers.AppController import AppController

from src.views.AnalyseView import AnalyseView
from src.views.AddReceiptView import AddReceiptView
from src.views.HistoryView import HistoryView
from src.views.LoginView import LoginView
from src.views.View import View



class MainView(View):
    """A class representing the main view of the application."""

    def __init__(self, canvas, root):
        """
        Initialize the MainView.

        Args:
            canvas (tk.Canvas): The canvas on which the view will be placed.
            root (tk.Tk): The root window of the application.
        """
        super().__init__(canvas)
        self.root = root

        currentDir = os.getcwd()
        self.logo = tk.PhotoImage(file=f"{currentDir}/src/icons/logo 256x256.png")
        self.logoLabel = ttk.Label(
            self.canvas, image=self.logo, padding=0, justify=tk.CENTER
        )

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

        self.historyButton = ttk.Button(self.navbarFrame, text="History")
        self.historyButton.configure(
            bootstyle="outline",
            command=lambda: Navigator().navigateTo(HistoryView(self.canvas)),
        )

        self.loginButton = ttk.Button(self.navbarFrame, text="Login")
        self.loginButton.configure(
            bootstyle="outline",
            command=lambda: Navigator().navigateTo(
                LoginView(self.canvas, "email", "password")
            ),
        )

        self.logoutButton = ttk.Button(self.navbarFrame, text="Logout")
        self.logoutButton.configure(
            bootstyle="outline-danger",
            command=lambda: AppController.logout(mainView = self),
        )

        self.quitButton = ttk.Button(self.navbarFrame, text="Quit")
        self.quitButton.configure(
            bootstyle="outline-danger", command=lambda: self.root.quit()
        )

    def place(self):
        """Place the main view elements on the canvas."""
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.logoLabel.place(x=30, y=50, width=260, height=260)

        self.navbarFrame.place(x=0, y=450, width=320, height=250)

        self.analyseButton.place(x=10, y=0, width=300, height=40)
        self.addReceiptButton.place(x=10, y=50, width=300, height=40)
        self.historyButton.place(x=10, y=100, width=300, height=40)

        if AppController.loggedIn:
            self.logoutButton.place(x=10, y=150, width=300, height=40)
        else:
            self.loginButton.place(x=10, y=150, width=300, height=40)

        self.quitButton.place(x=10, y=200, width=300, height=40)

    def hide(self):
        """Hide the main view elements from the canvas."""
        self.navbarFrame.place_forget()

        self.logoLabel.place_forget()

        self.analyseButton.place_forget()
        self.addReceiptButton.place_forget()
        self.historyButton.place_forget()
        self.loginButton.place_forget()
        self.logoutButton.place_forget()
        self.quitButton.place_forget()
