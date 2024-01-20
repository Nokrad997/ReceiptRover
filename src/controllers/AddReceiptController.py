from tkinter import filedialog
from PIL import Image, ImageTk

# from src.views.AddReceiptView import AddReceiptView
from src.views.View import View

class AddReceiptController:
    def __init__(self, addReceiptView: View):
        self.addReceiptView = addReceiptView
        self.image = None
    
    def openDialog(self):
        dialog = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Image files", ("*.jpg", "*.jpeg", "*.png")), ("all files", "*.*")))
        # print(dialog)
        # print(self.addReceiptView)
        self.image = Image.open(fp=dialog, mode="r")
        self.addReceiptView.hideFrame()
        self.addReceiptView.showImage(self.image)