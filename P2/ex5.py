from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 20000
IP = "127.0.0.1"

# -- Create a client object
c = Client(IP, PORT)

print(c.talk("Sending the U5 Gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))