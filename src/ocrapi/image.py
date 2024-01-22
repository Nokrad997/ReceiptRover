import cv2


class Image:
    """
    Represents an image object.

    Attributes:
        file (str): The file path of the image.
        image: The image data loaded from the file.

    Methods:
        getImage(): Returns the image data.
        setImage(image): Sets the image data.
        getFile(): Returns the file path of the image.
        setFile(file): Sets the file path of the image.
    """

    def __init__(self, file):
        self.file = file
        try:
            self.image = cv2.imread(self.file)
        except Exception as e:
            self.image = f"Error occurred while opening image: {e}"

    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image

    def getFile(self):
        return self.file

    def setFile(self, file):
        self.file = file
