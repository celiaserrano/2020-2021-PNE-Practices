from Client0 import Client


PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 20000
IP = "127.0.0.1"

# -- Create a client object
c = Client(IP, PORT)


c.advanced_ping()
c.ping()
print(f"IP: {c.ip}, {c.port}")

