from abc import abstractmethod

from MyCanvas import *


class Module(object):
    def __init__(self):
        self.root = MyCanvas.root
        self.root.attributes('-alpha', 0.3)
        self.canvas = MyCanvas.create(self.root)
        self.OverLap = False

    def getCanvas(self):
        return self.canvas

    @abstractmethod
    def drawMe(self):
        pass