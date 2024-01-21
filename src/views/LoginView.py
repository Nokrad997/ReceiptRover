import tkinter as tk
from ttkbootstrap import ttk

from src.Navigator import Navigator
from src.views.View import View
from src.controllers.AppController import AppController


class LoginView(View):
    def __init__(self, canvas, email, password):
        super().__init__(canvas)
        self.email = email
        self.password = password

        self.loginLabel = ttk.Label(self.canvas, text="Email")
        self.loginEntry = ttk.Entry(self.canvas)
        self.passwordLabel = ttk.Label(self.canvas, text="Password")
        self.passwordEntry = ttk.Entry(self.canvas)

        self.loginButton = ttk.Button(self.canvas, text="Login")
        self.registerButton = ttk.Button(self.canvas, text="Register")
        self.registerButton.configure(bootstyle="outline")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.loginLabel.place(x=60, y=150, width=200, height=20)
        self.loginEntry.place(x=60, y=170, width=200, height=30)
        self.passwordLabel.place(x=60, y=210, width=200, height=20)
        self.passwordEntry.place(x=60, y=230, width=200, height=30)

        self.loginButton.place(x=60, y=290, width=200, height=30)
        self.registerButton.place(x=60, y=330, width=200, height=30)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        # self.canvas.place_forget()

        self.loginLabel.place_forget()
        self.loginEntry.place_forget()
        self.passwordLabel.place_forget()
        self.passwordEntry.place_forget()

        self.loginButton.place_forget()
        self.registerButton.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()
