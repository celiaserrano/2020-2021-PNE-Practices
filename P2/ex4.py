from Client0 import Client
from termcolor import colored

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 20000
IP = "127.0.0.1"

# -- Create a client object
c = Client(IP, PORT)

print(c.debug_talk(colored("Message sent from the Client to the server", "blue", )))