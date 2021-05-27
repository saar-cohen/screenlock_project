from tkinter import *
from selectEx import *
from animation import *
import math

class NetworkGUIHandler:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Animation Server")
        self.canvas = Canvas(self.tk, width=300, height=200)
        self.canvas.pack()

        self.computer_address_list = []
        self.animation_iteration_number = 0

        # self.list_box = Listbox(self.canvas)
        # self.list_box.bind('<<ListboxSelect>>', self.onselect)
        # self.list_box.pack()
        self.sinMode = False
        self.selected_value = None

        self.mySelect = SelectEx()
        #self.client = Client()
        self.tk.after(10, self.selectIteration)

        self.animation_iteration_number = 0

        width = self.tk.winfo_screenwidth()
        height = self.tk.winfo_screenheight()
        self.animation = Animation(width, height)

        self.animation_mode = False

        self.buttons_to_remove_at_end_of_animation = []

    def addButton(self, text, button_width, button_command):
        button = Button(self.canvas, text=text, width=button_width, command=button_command)
        button.pack()

    def addAddress(self, computer_address):
        self.computer_address_list.append(computer_address)

    def startAnimation(self):
        print ("START ANIMATION")
        #self.animation_iteration_number = 0
        self.animation_mode = True
        self.tk.after(20, self.animationIteration)

    def stopAnimation(self):
        print ("STOP ANIMATION")
        self.animation_mode = False

    def animationIteration(self):
        self.animation_iteration_number = self.animation.iteration(self.computer_address_list, self.animation_iteration_number)
        for obj in self.animation.getDrawableObjects():
            if self.mySelect.sendObject(obj) is False:
                self.buttonDisconnected(obj.getClientAddress())
        if self.animation_mode:
            self.tk.after(20, self.animationIteration)
        else:
            self.removeDisconnectedButton()


    def removeDisconnectedButton(self):
        for address in self.buttons_to_remove_at_end_of_animation:
            for x in self.canvas.winfo_children():
                if x["text"].decode() == "{0} {1}".format(address[0], str(address[1])):
                    x.destroy()
            self.computer_address_list.remove(address)

    def SinModeOn(self):
        if self.sinMode == True:
            self.sinMode = False
        else:
            self.sinMode = True
        for x in self.canvas.winfo_children():
            if x["text"] ==  "Animatio Mode: Sinus":
                x["text"]= "Animatio Mode: Regular"
            elif x["text"] ==  "Animatio Mode: Regular":
                x["text"] = "Animatio Mode: Sinus"
        self.animation.setSinMode(self.sinMode)


    def buttonDisconnected(self,address):
        for x in self.canvas.winfo_children():
            print (x["text"])
            print ("{0} {1}".format(address[0], str(address[1])))
            if x["text"].decode() == "{0} {1}".format(address[0], str(address[1])) and x["bg"] != "lightskyblue4":
                x["bg"] =  "lightskyblue4"
                self.buttons_to_remove_at_end_of_animation.append(address)


           # if str(x["text"])
           # print "{0} {1}".format(address[0], str(address[1]))

    def selectIteration(self):
        newComputers = self.mySelect.selectIteration()
        for x in newComputers:
            self.addAddress(x)
            self.addButton(x, 15, None)

        self.tk.after(10, self.selectIteration)

    def mainloop(self):
        Tk().mainloop()


if __name__ == '__main__':

    networkGUIhandler = NetworkGUIHandler()

    networkGUIhandler.addButton("Start", 40, networkGUIhandler.startAnimation)
    networkGUIhandler.addButton("Stop", 40, networkGUIhandler.stopAnimation)
    networkGUIhandler.addButton("Animatio Mode: Regular", 40, networkGUIhandler.SinModeOn)
    networkGUIhandler.mainloop()