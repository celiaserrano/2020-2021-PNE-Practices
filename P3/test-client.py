from Client0 import Client
from pathlib import Path
from Seq1 import Seq

print(f"-----| Practice 3, Exercise 7 |------")

PORT = 2000
IP = "127.0.0.1"
print("Connection to SERVER at " + str(IP) + ", PORT: " + str(PORT))


gene_list = ["U5", "ADA", "FRAT1", "FXN"]
c = Client(IP, PORT)

print("* Testing PING...")
response = c.talk("PING")
print(response)

print("* Testing GET...")
seq = c.talk("GET 0")
seq1 = c.talk("GET 1")
seq2 = c.talk("GET 2")
seq3 = c.talk("GET 3")
seq4 = c.talk("GET 4")
print("GET 0: " + str(seq))
print("GET 1: " + str(seq1))
print("GET 2: " + str(seq2))
print("GET 3: " + str(seq3))
print("GET 4: " + str(seq))

print("* Testing INFO...")
seq = str(seq)
response = c.talk("INFO " + seq)
print(response)

print("* Testing COMP...")
seq = str(seq)
response = c.talk("COMP " + seq)
print(response)


print("* Testing REV...")
seq = str(seq)
response = c.talk("REV " + seq)
print(response)

print("* Testing GENE...")
for gene in gene_list:
    response = c.talk("GENE " + gene)
    print(response)