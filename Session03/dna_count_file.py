def correct_seq(DNA):
    for e in DNA:
        if e != "A" and e!= "C" and e != "G" and e != "T":
            return False
    return True



def counter_dna(DNA):
    a = 0
    c = 0
    g = 0
    t = 0
    for i in DNA:
        if i == "A":
            a = a + 1
        elif i == "C":
            c = c + 1
        elif i == "T":
            t = t + 1
        else:
            g = g + 1

    return a, c, g, t

def read_from_file(filename):
    with open(filename, 'r') as f:
        DNA = f.read()
        DNA.replace("\n", "")
        return DNA





DNA = read_from_file("dna.txt")
correct_dna = correct_seq(DNA)
if correct_dna:
    print("Total lenght of the sequence: ", len(DNA))
    a, c, g, t = counter_dna(DNA)
    print("A: ", a)
    print("C: ", c)
    print("G: ", g)
    print("T: ", t)

else:
    print("Not a valid DNA sequence")