from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 20000
IP = "127.0.0.1"

# -- Create a client object
c = Client(IP, PORT)
response = c.talk("Message")
print("Response: ", response)