from tkinter import filedialog

from src.views.AddReceiptView import AddReceiptView

class AddReceiptController:
    def __init__(self, addReceiptView : AddReceiptView):
        self.addReceiptView = AddReceiptView
    
    def openDialog(self):
        dialog = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Image files", ("*.jpg", "*.jpeg", "*.png")), ("all files", "*.*")))
        print(dialog)