import tkinter as tk
import ttkbootstrap as ttk

from src.views.View import View


class Navigator:
    stack = []

    @staticmethod
    def navigateTo(view: View):
        """
        Navigates to the specified view.

        Args:
            view (View): The view to navigate to.
        """
        if len(Navigator.stack) > 0:
            Navigator.stack[-1].hide()
        Navigator.stack.append(view)
        view.place()

    @staticmethod
    def navigateBack():
        """
        Navigates back to the previous view.
        """
        if len(Navigator.stack) > 1:
            Navigator.stack[-1].hide()
            Navigator.stack.pop()
            Navigator.stack[-1].place()
