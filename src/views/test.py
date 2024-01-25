import os
from PIL import Image, ImageTk

fullPath = os.getcwd() + "/" + chartPath
image = Image.open(fullPath, mode="r")
labelImage = ImageTk.PhotoImage(image)
self.chartLabel.configure(image=labelImage)