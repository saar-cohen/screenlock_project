import socket
import select
#from animation import *

class ClientData:
    def __init__(self, sock, address):
        self.sock = sock
        self.address = address

class SelectEx:
    def __init__(self):

        self.server_socket = socket.socket()
        self.server_socket.bind(('0.0.0.0', 8800))
        self.server_socket.listen(5)
        self.open_client_sockets = []
        self.messages_to_send = []
        self.clients_dict = {}


    def send_waiting_messages(self, wlist):
        for message in self.messages_to_send:
            (client_socket,data) = message
            if client_socket in wlist:
                client_socket.send(data)
                self.messages_to_send.remove(message)

    def selectIteration(self):
        newClients = []
        rlist, wlist, xlist = select.select([self.server_socket] + self.open_client_sockets, self.open_client_sockets,[], 0.1)
        for current_socket in rlist:
            if current_socket is self.server_socket:
                (new_socket,address) = self.server_socket.accept()
                print ("address {0} connected".format(address))
                newClients.append(address)
                self.open_client_sockets.append(new_socket)
                self.clients_dict[address] = ClientData(new_socket, address)


            else:
                try:
                    data = current_socket.recv(1024)
                except socket.error:
                    pass


        return newClients

    def sendObject(self, obj):
        try:
            address = obj.getClientAddress()
            client_data = self.clients_dict[address]
            client_data.sock.send(obj.dataToSend().ljust(max(1024,0)))
            return True
        except socket.error:
            if client_data.sock in self.open_client_sockets:
                self.open_client_sockets.remove(client_data.sock)
            return False