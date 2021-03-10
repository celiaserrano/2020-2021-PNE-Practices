from Seq1 import test_sequences

def print_results(i, sequence):
    print("Sequence" + str(i) + ": (lenght:" + str(sequence.len()) + ") " + str(sequence))
    print("Bases: ", sequence.count())
    print("Rev: ", sequence.reverse())


print("-----| Practice 1, Exercise 7 |------")

list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_results(i, list_sequences[i])
