import tkinter as tk
import ttkbootstrap as ttk
from src.Navigator import Navigator
from src.views.MainView import MainView

windows = ttk.Window(themename="superhero")
windows.title("Test")
windows.geometry("321x694")
windows.resizable(False, False)

mainViewCanvas = tk.Canvas(windows)
mainView = MainView(mainViewCanvas)
Navigator().navigateTo(mainView)

windows.mainloop()