"""
Represents a view for user registration.

Args:
    name (str): The name of the user.
    email (str): The email address of the user.
    password (str): The password of the user.
    retypePassword (str): The re-typed password for confirmation.

Attributes:
    name (str): The name of the user.
    email (str): The email address of the user.
    password (str): The password of the user.
    reTypePassword (str): The re-typed password for confirmation.
"""

import tkinter as tk
from ttkbootstrap import ttk

from src.Navigator import Navigator

from src.controllers.AppController import AppController

from src.views.View import View


class RegistrationView(View):
    """
    A class representing the login view of the application.

    Args:
        canvas (tkinter.Canvas): The canvas on which the view will be placed.
        email (str): The email entered by the user.
        password (str): The password entered by the user.
    """

    def __init__(self, canvas):
        super().__init__(canvas)

        self.registrationLabel = ttk.Label(self.canvas, font=("Helvetica", 16), text="Registration")

        self.nameLabel = ttk.Label(self.canvas, text="Username")
        self.nameEntry = ttk.Entry(self.canvas)
        self.emailLabel = ttk.Label(self.canvas, text="Email")
        self.emailEntry = ttk.Entry(self.canvas)
        self.passwordLabel = ttk.Label(self.canvas, text="Password")
        self.passwordEntry = ttk.Entry(self.canvas)
        self.reTypePasswordLabel = ttk.Label(self.canvas, text="Repeat password")
        self.reTypePasswordEntry = ttk.Entry(self.canvas)

        self.registerButton = ttk.Button(self.canvas, text="Register")
        self.registerButton.configure(bootstyle="primary", command=lambda: AppController().register(self))

        self.navbarFrame = ttk.Frame(self.canvas)

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        """
        Places the login view on the canvas.
        """
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.registrationLabel.place(x=10, y=10, width=300, height=40)

        self.nameLabel.place(x=60, y=150, width=200, height=20)
        self.nameEntry.place(x=60, y=170, width=200, height=30)
        self.emailLabel.place(x=60, y=210, width=200, height=20)
        self.emailEntry.place(x=60, y=230, width=200, height=30)
        self.passwordLabel.place(x=60, y=270, width=200, height=20)
        self.passwordEntry.place(x=60, y=290, width=200, height=30)
        self.reTypePasswordLabel.place(x=60, y=330, width=200, height=20)
        self.reTypePasswordEntry.place(x=60, y=350, width=200, height=30)

        self.registerButton.place(x=60, y=410, width=200, height=30)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        """
        Hides the login view from the canvas.
        """
        self.registrationLabel.place_forget()
        
        self.nameLabel.place_forget()
        self.nameEntry.place_forget()
        self.emailLabel.place_forget()
        self.emailEntry.place_forget()
        self.passwordLabel.place_forget()
        self.passwordEntry.place_forget()
        self.reTypePasswordLabel.place_forget()
        self.reTypePasswordEntry.place_forget()

        self.registerButton.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()

