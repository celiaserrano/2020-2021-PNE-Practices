
test = input("Testing: ")
print("* Testing " + str(test) + "...")
if test == "PING":
    print("OK!")

elif test == "GET":
    print("GET 0: " + str(list_sequences[0]) + "\nGET 1: " + str(list_sequences[1]) + "\nGET 2: " + str(list_sequences[2]) + "\nGET 3: " + str(list_sequences[3]) + "\nGET 4: " + str(list_sequences[4]))

elif test == "INFO":

    print("Sequence: " + str(seq) + "\nTotal lenght: " + str(seq.len()) + str(seq.percent()))

elif test == "COMP":
    print(str(seq) + str(seq.complement()))

elif test == "REV":
    print(str(seq) + str(seq.reverse()))

