import tkinter as tk
from ttkbootstrap import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

# from src.views.AddReceiptView import AddReceiptView
from src.views.View import View


class AddReceiptController:
    def __init__(self, addReceiptView: View):
        self.addReceiptView = addReceiptView
        self.image = None

    def openDialog(self):
        dialog = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(
                ("Image files", ("*.jpg", "*.jpeg", "*.png")),
                ("all files", "*.*"),
            ),
        )
        self.image = Image.open(fp=dialog, mode="r")
        self.addReceiptView.hideFrame()
        self.addReceiptView.showImage(self.image)

    def addProduct(self):
        childrensLength = len(self.addReceiptView.scrollableList.children)
        pixelsToAdd = 50 * (childrensLength // 3)

        try:
            entry = ttk.Entry(self.addReceiptView.scrollableList)
            count = ttk.Entry(self.addReceiptView.scrollableList)
            price = ttk.Entry(self.addReceiptView.scrollableList)

        except tk.TclError as e:
            print(f"An error occurred during widget creation: {e}")

            entry.destroy()
            count.destroy()
            price.destroy()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

            entry.destroy()
            count.destroy()
            price.destroy()

        else:
            entry.place(x=10, y=pixelsToAdd, width=180, height=40)
            count.place(x=200, y=pixelsToAdd, width=45, height=40)
            price.place(x=255, y=pixelsToAdd, width=45, height=40)
