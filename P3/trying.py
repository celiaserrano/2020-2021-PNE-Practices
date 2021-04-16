#MÁS INTENTOS
test = input("Testing: ")
print("* Testing " + str(test) + "...")
if test == "PING":
    print(c.talk("OK!"))

elif test == "GET":
    print(c.talk("GET 0: " + str(list_sequences[0]) + "\nGET 1: " + str(list_sequences[1]) + "\nGET 2: " + str(list_sequences[2]) + "\nGET 3: " + str(list_sequences[3]) + "\nGET 4: " + str(list_sequences[4])))

elif test == "INFO":

    print(c.talk("Sequence: " + str(seq) + "\nTotal lenght: " + str(seq.len()) + str(seq.percent())))



elif test == "COMP":
    print(c.talk(str(seq) + str(seq.complement())))

elif test == "REV":
    print(c.talk(str(seq) + str(seq.reverse())))

elif test == "GENE":

    for gene in gene_list:
        response = Seq()
        response.read_fasta(gene + ".txt")
        response = str(response)
        print("GENE " + str(gene) + "\n" + str(response))
        print(c.talk(response))




