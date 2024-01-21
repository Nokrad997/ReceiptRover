import tkinter as tk
import ttkbootstrap as ttk
from src.Navigator import Navigator
from src.views.MainView import MainView

<<<<<<< HEAD
windows = ttk.Window(themename="superhero")
windows.title("Test")
windows.geometry("320x700")
windows.resizable(False, False)

mainViewCanvas = tk.Canvas(windows)
mainView = MainView(mainViewCanvas)
=======
root = ttk.Window(themename="superhero")
root.title("Test")
root.geometry("320x700")
root.resizable(False, False)

mainViewCanvas = tk.Canvas(root)
mainView = MainView(mainViewCanvas, root)
>>>>>>> add-receipt-controller
Navigator().navigateTo(mainView)

root.mainloop()
