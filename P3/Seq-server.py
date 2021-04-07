import socket
import server_utils


list_sequences = ["ACACACACGAGAGGATTATATCCTT", "GGGGGTTTTAAAAACCTTAGATCAT", "CAGATAGATATAGAGATCACAC", "AAAAATTTTTTGGGCCCCC", "TTCCCGGGGTTTGGGCCCTTTAA"]
# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
ls.accept()

print("A client has connected to the server!")

# -- Close the socket
ls.close()

while True:
    try:
        (cs, client_ip_port) = ls.accept()
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    # -- Execute this part if there are no errors

        # -- Read the message from the client
        # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)
    print(msg_raw)

        # -- We decode it for converting it
        # -- into a human-redeable string
    msg = msg_raw.decode()
    formatted_message = server_utils.format_command(msg)
    print(formatted_message)
    formatted_message = formatted_message.split(" ")
    if len(formatted_message) == 1:
        command = formatted_message[0]

    else:
        command = formatted_message[0]
        argument = formatted_message[1]

    if formatted_message == "PING":
        server_utils.ping(cs)

    elif command == "GET":
        server_utils.get(cs, list_sequences, argument)


    else:
        response = "Not avaible command"
        cs.send(str(response.encode()))

    cs.close()

    if count_connections == 5:
       for i in range(0, len(client_address_list)):
            print("Client " + str(i) + ": Client IP, PORT: " + str(client_address_list[i]))
       exit(0)