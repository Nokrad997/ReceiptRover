import tkinter as tk
import ttkbootstrap as ttk
from src.Navigator import Navigator
from src.views.MainView import MainView

root = ttk.Window(themename="superhero")
root.title("ReceiptRover")
root.geometry("320x700")
root.resizable(False, False)

# print(bcrypt.checkpw('testtest'.encode('utf-8'), "$2b$12$b6derw0r4Sw2wYE0C2GuU.ecVTku5uzGQtvw3YO/ZyIvYNTJTyLQW".encode('utf-8')))
# print(bcrypt.checkpw('testtest'.encode('utf-8'), "$2b$12$xqLrHQyUN5OOeDlCilkvFOe3GVr0/mG6tckQ2IQjiWgCTz8QhV8Bi".encode('utf-8')))

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
