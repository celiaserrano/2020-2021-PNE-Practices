import socket
from termcolor import colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
            s.close()

        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the Ip and the Port?")


    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)



    def talk(self, msg):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.


        print("To Server:", msg)

        s.send(msg.encode())

        # Receive data
        response = s.recv(2048).decode()

        s.close()
        return response

    def debug_talk(self, msg):
        return "From server: " + colored(self.talk(msg), "green", )


