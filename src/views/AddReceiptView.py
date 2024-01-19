import tkinter as tk
from ttkbootstrap import ttk

from src.controllers.AppController import AppController

from src.Navigator import Navigator
from src.views.View import View
class AddReceiptView(View):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.addReceiptLabel = ttk.Label(self.canvas, text="Add Receipt")
        self.addReceiptLabel.configure(bootstyle="primary")

        self.addReceiptButton = ttk.Button(self.canvas, text="Add Receipt", command=lambda: self.openDialog()) 
        self.addReceiptButton.configure(bootstyle="primary")

        self.pathLabel = ttk.Label(self.canvas, text="Path")

        self.navbarFrame = ttk.Frame(self.canvas)
        self.navbarFrame.configure(bootstyle="sucess")

<<<<<<< Updated upstream
=======
        self.navbarLabel = ttk.Label(self.navbarFrame, text="Take photo of receipt or import image", anchor=tk.CENTER)

        self.cameraIcon = tk.PhotoImage(file=f"{self.currentPath}\src\icons\camera 30x30.png")
        self.cameraButton = ttk.Button(self.navbarFrame, compound=tk.TOP, image=self.cameraIcon, padding=3)
        self.cameraButton.configure(bootstyle="outline")

        self.imageIcon = tk.PhotoImage(file=f"{self.currentPath}\src\icons\image 30x30.png")
        self.importImageButton = ttk.Button(self.navbarFrame, compound=tk.TOP, image=self.imageIcon, padding=3)
        self.importImageButton.configure(bootstyle="outline", command=lambda: AppController.openDialog(addReceiptView=self))

>>>>>>> Stashed changes
        self.backButton = ttk.Button(self.navbarFrame, text="Back")
        self.backButton.configure(bootstyle="outline", command=lambda: Navigator().navigateBack())

    def place(self):
        self.canvas.place(x=0, y=0, width=321, height=694)
        
        self.addReceiptLabel.place(x=60, y=145, width=200, height=20)
        self.addReceiptButton.place(x=60, y=165, width=200, height=30)

        self.navbarFrame.place(x=0, y=624, width=321, height=50)

    def hide(self):
        self.addReceiptLabel.place_forget()
        self.addReceiptButton.place_forget()

        self.navbarFrame.place_forget()
<<<<<<< Updated upstream
        self.backButton.place_forget()

    def openDialog(self):
        dialog = 
=======
        self.navbarLabel.place_forget()

        self.cameraButton.place_forget()
        self.importImageButton.place_forget()
        self.backButton.place_forget()
>>>>>>> Stashed changes
