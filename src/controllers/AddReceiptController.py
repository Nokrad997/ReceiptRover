from tkinter import filedialog

# from src.views.AddReceiptView import AddReceiptView
from src.views.View import View

class AddReceiptController:
    def __init__(self):
        pass
    
    def openDialog(self, addReceiptView: View):
        dialog = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Image files", ("*.jpg", "*.jpeg", "*.png")), ("all files", "*.*")))
        print(dialog)
        print(addReceiptView)