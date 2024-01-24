import tkinter as tk
from ttkbootstrap import ttk

from src.Navigator import Navigator

from src.controllers.AppController import AppController

from src.views.RegistrationView import RegistrationView
from src.views.View import View


class LoginView(View):
    """
    A class representing the login view of the application.

    Args:
        canvas (tkinter.Canvas): The canvas on which the view will be placed.
        email (str): The email entered by the user.
        password (str): The password entered by the user.
    """

    def __init__(self, canvas, email, password):
        super().__init__(canvas)
        self.email = email
        self.password = password

        self.loginMainLabel = ttk.Label(self.canvas, font=("Helvetica", 16), text="Login")

        self.loginLabel = ttk.Label(self.canvas, text="Email")
        self.loginEntry = ttk.Entry(self.canvas)
        self.passwordLabel = ttk.Label(self.canvas, text="Password")
        self.passwordEntry = ttk.Entry(self.canvas)

        self.loginButton = ttk.Button(self.canvas, text="Login")
        self.registerButton = ttk.Button(self.canvas, text="Register", command=lambda: Navigator().navigateTo(RegistrationView(self.canvas)))
        self.registerButton.configure(bootstyle="outline")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        """
        Places the login view on the canvas.
        """
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.loginMainLabel.place(x=10, y=10, width=300, height=40)

        self.loginLabel.place(x=60, y=150, width=200, height=20)
        self.loginEntry.place(x=60, y=170, width=200, height=30)
        self.passwordLabel.place(x=60, y=210, width=200, height=20)
        self.passwordEntry.place(x=60, y=230, width=200, height=30)

        self.loginButton.place(x=60, y=290, width=200, height=30)
        self.registerButton.place(x=60, y=330, width=200, height=30)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        """
        Hides the login view from the canvas.
        """
        self.loginMainLabel.place_forget()

        self.loginLabel.place_forget()
        self.loginEntry.place_forget()
        self.passwordLabel.place_forget()
        self.passwordEntry.place_forget()

        self.loginButton.place_forget()
        self.registerButton.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()
