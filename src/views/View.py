from abc import ABC, abstractmethod

class View(ABC):
    def __init__(self, canvas):
        self.canvas = canvas

    @abstractmethod
    def place():
        pass

    # @abstractmethod
    # def update():
    #     pass