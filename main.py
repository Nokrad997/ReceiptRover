import tkinter as tk
import ttkbootstrap as ttk
from src.Navigator import Navigator
from src.views.MainView import MainView

root = ttk.Window(themename="superhero")
root.title("ReceiptRover")
root.geometry("320x700")
root.resizable(False, False)

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
