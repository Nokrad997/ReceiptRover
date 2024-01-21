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
        self.loginButton.configure(bootstyle="outline", command=lambda: self.loginClicked())
        self.registerButton = ttk.Button(self.canvas, text="Register")
        self.registerButton.configure(bootstyle="outline")


        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(bootstyle="outline", command=lambda: Navigator().navigateBack())


    def place(self):
        self.canvas.place(x=0, y=0, width=321, height=694)
        
        self.loginLabel.place(x=60, y=145, width=200, height=20)
        self.loginEntry.place(x=60, y=165, width=200, height=30)
        self.passwordLabel.place(x=60, y=205, width=200, height=20)
        self.passwordEntry.place(x=60, y=225, width=200, height=30)

        self.loginButton.place(x=60, y=285, width=200, height=30)
        self.registerButton.place(x=60, y=325, width=200, height=30)

        self.navbarFrame.place(x=0, y=624, width=321, height=50)
        self.backButton.place(x=7, y=10, width=321-14, height=40)

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

    def loginClicked(self):
        self.email = self.loginEntry.get()
        self.password = self.passwordEntry.get()
        AppController().login(self)