from src.scannerModule.ImageTransformation import TransformImage


class Scanner:
    def __init__(self, file_path):
        """
        Initializes a Scanner object.

        Args:
            file_path (str): The path to the image file to be scanned.

        Raises:
            ValueError: If an error occurs while opening the image.
        """
        self.file_path = file_path
        try:
            self.transform = TransformImage(self.file_path)
        except Exception as e:
            raise ValueError(f"Error occurred while opening image: {e}")

    def scan(self):
        """
        Performs the scanning process on the image.

        Raises:
            ValueError: If an error occurs while scanning.
            ValueError: If an error occurs while correcting perspective.
        """
        try:
            self.transform.resizeImage()
            self.transform.toGray()
            self.transform.blurGray()
            self.transform.detectEdges()
            self.transform.findContours()
            try:
                self.transform.correctPerspective()
            except InterruptedError:
                self.transform.manualContourSelection()
                self.transform.correctPerspective()
            except Exception as e:
                print(e)
                raise ValueError(f"Error occurred while correcting perspective: {e}")

            self.transform.toBlackAndWhite()
        except Exception as e:
            raise ValueError(f"Error occurred while scanning: {e}")

    def saveScanned(self, file_path):
        """
        Saves the scanned image to a file.

        Args:
            file_path (str): The path to save the scanned image.

        Returns:
            bool: True if the image is successfully saved, False otherwise.

        Raises:
            ValueError: If an error occurs while saving the image.
        """
        try:
            return self.transform.saveImage(file_path)
        except Exception as e:
            raise ValueError(f"Error occurred while saving image: {e}")
