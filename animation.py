#from RectModule import *
import time
#from Client.Client import *
import math


class DrawableObject:
    def __init__(self, x1, y1, x2 , y2, client):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.client = client
        pass

    def getClientAddress(self):
        return self.client

    def dataToSend(self):
        return "animation-{0}:{1}-{2}:{3}".format(self.x1, self.y1, self.x2, self.y2)

class Animation():


    def __init__(self, width, height):
        self.drawableObjects = []
        self.x1 = 0
        self.y1 = height/2 - 100
        self.x2 = 300
        self.y2 = height/2 + 100
        self.a = 10
        self.b = 0
        self.width = width
        self.height = height
        self.t = 0
        self.t_step = 5
        self.sin_mode = False
        self.delta_t = 0

    def setSinMode(self, sin_mode):
        self.sin_mode = sin_mode

    def calcT(self):
        tRadians = math.radians(self.t)
        value = int(math.sin(tRadians) * 100)
        return value

    def iteration(self, clients, i):
        # reset animation list
        self.drawableObjects = []

        if self.sin_mode == True:
            self.delta_t = self.calcT()
            print (self.delta_t)


        print ("before {0}, {1} - {2}, {3}".format(self.x1, self.y1 + self.delta_t, self.x2, self.y2+ self.delta_t))
        self.x1 = self.x1 + self.a
        self.y1 = self.y1 + self.b
        self.x2 = self.a + self.x2
        self.y2 = self.b + self.y2
        print ("after {0}, {1} - {2}, {3}".format(self.x1, self.y1+self.delta_t, self.x2, self.y2+self.delta_t))

        if (self.x1 >= self.width):
            self.drawableObjects.append(DrawableObject(self.x1, self.y1+self.delta_t, self.x2, self.y2+self.delta_t, clients[i]))

            self.x1 = self.x1 - self.width
            self.x2 = self.x2 - self.width

            i = (i + 1) % len(clients)
            print ("modulu {0}, {1} - {2}, {3}".format(self.x1, self.y1+self.delta_t, self.x2, self.y2+self.delta_t))

        self.drawableObjects.append(DrawableObject(self.x1, self.y1+self.delta_t, self.x2, self.y2+self.delta_t, clients[i]))

        #at overlap
        if (self.x2 >= self.width and self.x1 < self.width):
            self.drawableObjects.append(DrawableObject(max(self.x1 - self.width, 0), self.y1+self.delta_t, self.x2 - self.width, self.y2+self.delta_t, clients[(i + 1) % len(clients)]))

        if self.sin_mode == True:
            self.t += self.t_step

        return i

    def getDrawableObjects(self):
        return self.drawableObjects

    # def sendDrawable(self, clients):
    #     for obj in self.drawableObjects:
    #         print("client {0} -- rectangle {1}-{2} ... {3}-{4}".format(obj.client, obj.x1, obj.y1, obj.x2, obj.y2))
    #         # send to the clients in the list
    #         for x in clients:
    #             x.send(obj)




    def mainLoop(self, clients):
        i = 0
        while True:
            i = self.iteration(clients, i)
            self.sendDrawable(clients)
            print ("--------- end iter --------------")
            time.sleep(0.05)


def main():
    import Client
    my_animation = Animation()
    clients = []
    clients.append(Client().newClient())
    my_animation.mainLoop(clients)

if __name__ == '__main__':
    main()