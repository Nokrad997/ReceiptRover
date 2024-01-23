import tkinter as tk
import ttkbootstrap as ttk
from src.Navigator import Navigator
from src.views.MainView import MainView
from src.views.RegistrationView import RegistrationView

# rv = RegistrationView("test", "test@log1.pl", "testtest", "testtest")
# rc = RegistrationController(rv, usr)


# usr = User(id=1, name="cipa", email="test@test.pl", password="testtest")

# lv = LoginView("test@log1.pl", "testtest")
# lc = LoginController(lv, usr)

<<<<<<<<< Temporary merge branch 1
# print(lc.login())
=========
        PISZEMY KURWA CAMEL CASEM :)
        jebacZydow, a nie jebac_zydow
        zrobmy to porzadnie, a nie jakies gówno

'''

rv = RegistrationView("test1", "test@log1.pl", "testtest", "testtest")
rc = RegistrationController(rv, UserRepository())

print(rc.registerUser())

userRepository = UserRepository()

lv = LoginView("test@log1.pl", "testtest")
lc = LoginController(lv, userRepository)

print(lc.login())
>>>>>>>>> Temporary merge branch 2

# print(bcrypt.checkpw('testtest'.encode('utf-8'), "$2b$12$b6derw0r4Sw2wYE0C2GuU.ecVTku5uzGQtvw3YO/ZyIvYNTJTyLQW".encode('utf-8')))
# print(bcrypt.checkpw('testtest'.encode('utf-8'), "$2b$12$xqLrHQyUN5OOeDlCilkvFOe3GVr0/mG6tckQ2IQjiWgCTz8QhV8Bi".encode('utf-8')))

windows = ttk.Window(themename="superhero")
windows.title("Test")
windows.geometry("321x694")
windows.resizable(False, False)

mainViewCanvas = tk.Canvas(root)
mainView = MainView(mainViewCanvas, root)
Navigator().navigateTo(mainView)

root.mainloop()


# import requests


# for i in range(10):
#         try:
#                 response = requests.post('http://pythontess:5000', files={'file': open('scaned_test4.jpg', 'rb')})
#                 print(response.json())
#         except Exception as e:
#                 print(e)
