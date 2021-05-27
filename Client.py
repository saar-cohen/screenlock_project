import socket
import select
import tkinter
import time


class Client(object):

    def __init__(self):
        self.my_socket = socket.socket()

    def connect(self):

        self.my_socket.connect(('10.51.101.136', 8800))
        self.my_socket.send(socket.gethostname())

    def graphic_init(self):
        self.root = tkinter.Tk()
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.root, width=self.root.winfo_screenwidth(),
                                     height=self.root.winfo_screenheight())
        self.canvas.master.title("Canvas")
        self.canvas.pack()

    def run(self):

        rlist, wlist, xlist = select.select([self.my_socket], [], [], 0.1)
        for sock in rlist:
            data = self.my_socket.recv(1024)

            splitted_data = data.split("-")
            print
            "splited_data:"
            for i in splitted_data:
                print
                i
            print
            "--------------"

            p1_str = splitted_data[1]

            p2_str = splitted_data[2]

            p1_splitted = p1_str.split(":")
            p2_splitted = p2_str.split(":")

            x1 = int(p1_splitted[0])
            y1 = int(p1_splitted[1])
            x2 = int(p2_splitted[0])

            y2 = int(p2_splitted[1])

            print
            "{0}, {1} - {2}, {3}".format(x1, y1, x2, y2)
            self.canvas.delete("all")
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", fill="blue", width=2)

            print
            'the server sent:' + data

        self.root.after(10, self.run)

    def mainloop(self):
        self.root.after(10, self.run)
        self.root.mainloop()


def main():
    client = Client()
    client.connect()
    client.graphic_init()
    client.mainloop()


if __name__ == '__main__':
    main()