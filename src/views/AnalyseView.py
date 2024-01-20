import tkinter as tk
from ttkbootstrap import ttk

from src.Navigator import Navigator
from src.views.View import View


class AnalyseView(View):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.monthLabel = ttk.Label(self.canvas, text="Month")

        self.selected_month = tk.StringVar()  # Create a Tkinter variable
        # Category combobox
        self.monthMenuButton = ttk.Menubutton(
            self.canvas,
            bootstyle="outline-primary",
            state="readonly",
            textvariable=self.selected_month,  # Link the variable to the Menubutton
        )
        self.monthMenuButton.menu = tk.Menu(self.monthMenuButton, tearoff=0)
        self.monthMenuButton["menu"] = self.monthMenuButton.menu
        for month in [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
        ]:
            self.monthMenuButton.menu.add_radiobutton(
                label=month,
                value=month,
                variable=self.selected_month,
                command=lambda: self.prepareChart(self.selected_month.get()),
            )

        self.chartFrame = ttk.Frame(self.canvas)
        self.chartFrame.configure(bootstyle="sucess")

        # paste matplotlib chart into frame

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.monthLabel.place(x=60, y=165, width=200, height=20)
        self.monthMenuButton.place(x=60, y=185, width=200, height=30)

        self.chartFrame.place(x=10, y=225, width=300, height=300)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        self.monthLabel.place_forget()
        self.monthMenuButton.place_forget()

        self.chartFrame.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()

    def prepareChart(self, month):
        print(month)
