# import tkinter as tk
# import ttkbootstrap as ttk
# from src.Navigator import Navigator
# from src.views.MainView import MainView

# root = ttk.Window(themename="superhero")
# root.title("Test")
# root.geometry("320x700")
# root.resizable(False, False)

# mainViewCanvas = tk.Canvas(root)
# mainView = MainView(mainViewCanvas, root)
# Navigator().navigateTo(mainView)

# root.mainloop()


import requests

url = 'http://localhost:5000/ocr'
new_file = 'scaned_test4.jpg'
with open(new_file, 'rb') as f:
        files = {'file': (new_file, f)}
        # Make a POST request to the API
        response = requests.post(url, files=files)
print(response.json())