from tkinter import *
import tkinter as messagebox



class MyCanvas():
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    canvas = None
    list = []

    @staticmethod
    def create(tk):
        MyCanvas.canvas = Canvas(tk, width=MyCanvas.width, height=MyCanvas.height)
        MyCanvas.canvas.master.title("Canvas")
        MyCanvas.canvas.pack()
        return MyCanvas.canvas

    @staticmethod
    def getCanvas():
        return MyCanvas.canvas

    @staticmethod
    def addButton(text, button_width, button_command):
        button = Button(MyCanvas.root, text=text, width=button_width, command=button_command)
        button.pack()

    @staticmethod
    def onselect(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        messagebox.showinfo("Listbox Select", 'You selected listitem {0}: "{1}"'.format(index, value))

    @staticmethod
    def addList():
        MyCanvas.list_w = Listbox(MyCanvas.root)
        MyCanvas.list_w.bind('<<ListboxSelect>>', MyCanvas.onselect)
        MyCanvas.list_w.pack()


    @staticmethod
    def getList():
        return MyCanvas.list

    @staticmethod
    def addItem(item):
        if item in MyCanvas.list:
            return
        MyCanvas.list.append(item)
        #MyCanvas.list_w.insert(MyCanvas.list_w.size(), item)