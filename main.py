import tkinter as tk
import ttkbootstrap as ttk

# from src.models.Users import Users
# import bcrypt

# from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController

from src.Navigator import Navigator
from src.views.LoginView import LoginView
from src.views.MainView import MainView
from src.views.RegistrationView import RegistrationView

# rv = RegistrationView("test", "test@log1.pl", "testtest", "testtest")
# rc = RegistrationController(rv, usr)


# usr = User(id=1, name="cipa", email="test@test.pl", password="testtest")

# lv = LoginView("test@log1.pl", "testtest")
# lc = LoginController(lv, usr)

# print(lc.login())

# rv = RegistrationView("test1", "test@log1.pl", "testtest", "testtest")
# rc = RegistrationController(rv, UserRepository())

windows = ttk.Window(themename="superhero")
windows.title("Test")
windows.geometry("321x694")
windows.resizable(False, False)

mainViewCanvas = tk.Canvas(windows)
mainView = MainView(mainViewCanvas)
Navigator().navigateTo(mainView)

# loginViewCanvas = tk.Canvas(windows)
# loginView = LoginView(loginViewCanvas, "email", "password")

# registerViewCanvas = tk.Canvas(windows)
# registerView = RegistrationView(registerViewCanvas, "chuj", "chuj", "chuj", "chuj")

windows.mainloop()
