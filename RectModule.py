#authour saar
from Client import *
import MyCanvas


class RectModule(Module):

    def __init__(self):
        super(RectModule, self).__init__()
        self.x1 = 0
        self.y1 = 100
        self.x2 = 300
        self.y2 = 300
        self.a = 10
        self.b = 0


        self.overlap = False

    def drawMe(self):
        self.x1 = self.x1 + self.a
        self.y1 = self.y1 + self.b
        self.x2 = self.a + self.x2
        self.y2 = self.b + self.y2

        self.rect = self.getCanvas().delete("all")
        self.rect = self.getCanvas().create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                       outline="#f11", fill="blue", width=2)
        if self.overlap == True:
            self.rect = self.getCanvas().create_rectangle(self.x1 - MyCanvas.width, self.y1, self.x2 - MyCanvas.width, self.y2,
                                           outline="#f11", fill="blue", width=2)

        if (self.x2 == MyCanvas.width):
            self.overlap = True

        if (self.x1 >= MyCanvas.width):
            self.x1 = self.x1 - MyCanvas.width
            self.x2 = self.x2 - MyCanvas.width
            self.overlap = False

        self.getCanvas().after(10, self.drawMe)


if __name__ == '__main__':
    recti = RectModule()
    recti.root.after(10, recti.drawMe)
    recti.root.mainloop()
