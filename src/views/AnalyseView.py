import calendar
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from ttkbootstrap import ttk

from src.Navigator import Navigator
from src.views.View import View


class AnalyseView(View):
    """A class representing the AnalyseView in the ReceiptRover application."""

    def __init__(self, canvas):
        """
        Initialize the AnalyseView.

        Args:
            canvas (tk.Canvas): The canvas on which the view will be placed.
        """
        super().__init__(canvas)

        self.analyseLabel = ttk.Label(self.canvas, font=("Helvetica", 16), text="Analyse")

        self.selectedYear = tk.StringVar()  # Create a Tkinter variable
        self.selectedMonth = tk.StringVar()  # Create a Tkinter variable

        self.yearLabel = ttk.Label(self.canvas, text="Year")
        self.yearLabel.configure(justify=tk.CENTER)

        # Category combobox
        self.yearMenuButton = ttk.Menubutton(
            self.canvas,
            bootstyle="outline-primary",
            state="readonly",
            textvariable=self.selectedYear,  # Link the variable to the Menubutton
        )
        self.yearMenuButton.menu = tk.Menu(self.yearMenuButton, tearoff=0)
        self.yearMenuButton["menu"] = self.yearMenuButton.menu
        for year in [
            2023,
            2024,
        ]:
            self.yearMenuButton.menu.add_radiobutton(
                label=year,
                value=year,
                variable=self.selectedYear,
                command=lambda: self.unlockMonths(int(self.selectedYear.get())),
            )

        self.monthLabel = ttk.Label(self.canvas, text="Month")
        self.monthLabel.configure(justify=tk.CENTER)

        # Category combobox
        self.monthMenuButton = ttk.Menubutton(
            self.canvas,
            bootstyle="outline-primary",
            state="disabled",
            textvariable=self.selectedMonth,  # Link the variable to the Menubutton
        )
        self.monthMenuButton.menu = tk.Menu(self.monthMenuButton, tearoff=0)
        self.monthMenuButton["menu"] = self.monthMenuButton.menu


        self.chartFrame = ttk.Frame(self.canvas)
        self.chartFrame.configure(bootstyle="sucess")

        # paste matplotlib chart into frame

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(
            bootstyle="outline-danger", command=lambda: Navigator().navigateBack()
        )

    def place(self):
        """Place the AnalyseView on the canvas."""
        self.canvas.place(x=0, y=0, width=320, height=700)

        self.analyseLabel.place(x=10, y=10, width=300, height=40)

        self.yearLabel.place(x=60, y=170, width=200, height=20)
        self.yearMenuButton.place(x=60, y=190, width=200, height=30)

        self.monthLabel.place(x=60, y=230, width=200, height=20)
        self.monthMenuButton.place(x=60, y=250, width=200, height=30)

        self.chartFrame.place(x=10, y=290, width=300, height=300)

        self.navbarFrame.place(x=0, y=640, width=320, height=50)
        self.backButton.place(x=10, y=10, width=300, height=40)

    def hide(self):
        """Hide the AnalyseView."""
        self.analyseLabel.place_forget()

        self.yearLabel.place_forget()
        self.yearMenuButton.place_forget()
        
        self.monthLabel.place_forget()
        self.monthMenuButton.place_forget()

        self.chartFrame.place_forget()

        self.navbarFrame.place_forget()
        self.backButton.place_forget()

    def unlockMonths(self, year: int):
        self.monthMenuButton.configure(state="readonly")
        self.monthMenuButton.menu.delete(0, tk.END)

        if year == datetime.now().year:
            currentMonthIndex = datetime.now().month
            availableMonths = calendar.month_name[1:currentMonthIndex+1]
        else:
            availableMonths = calendar.month_name[1:]

        for month in availableMonths:
            self.monthMenuButton.menu.add_radiobutton(
                label=month,
                value=month,
                variable=self.selectedMonth,
                command=lambda: self.prepareChart(self.selectedMonth.get()),
            )

    def prepareChart(self, month):
        """
        Prepare the chart for the selected month.

        Args:
            month (str): The selected month.
        """
        print(month) 
