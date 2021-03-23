from Client0 import Client


PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 20000
IP = "127.0.0.1"

# -- Create a client object
c = Client(IP, PORT)
print(str(c))