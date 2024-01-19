import tkinter as tk
from ttkbootstrap import Window

from src.Navigator import Navigator

from src.views.MainView import MainView
<<<<<<< Updated upstream
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
=======
windows = Window(themename="superhero")
>>>>>>> Stashed changes
windows.title("Test")
windows.geometry("321x694")
windows.resizable(False, False)

mainViewCanvas = tk.Canvas(windows)
mainView = MainView(mainViewCanvas)
Navigator().navigateTo(mainView)

windows.mainloop()
