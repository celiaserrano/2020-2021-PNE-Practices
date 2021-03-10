from Seq1 import Seq

def print_results(sequence):
    print("Sequence"  + ": (lenght:" + str(sequence.len()) + ") " + str(sequence))
    print("Bases: ", sequence.count())
    print("Rev: ", sequence.reverse())
    print("Comp: ", sequence.complement())


print("-----| Practice 1, Exercise 9 |------")
s1 = Seq()
s1.read_fasta("ADA.txt")
print_results(s1)
