from src.scannerModule.ImageTransformation import TransformImage


class Scanner:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.transform = TransformImage(self.file_path)
        except Exception as e:
            raise ValueError(f"Error occurred while opening image: {e}")

    def scan(self):
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
        try:
            return self.transform.saveImage(file_path)
        except Exception as e:
            raise ValueError(f"Error occurred while saving image: {e}")
