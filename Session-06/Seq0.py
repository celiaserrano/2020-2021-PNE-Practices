from pathlib import Path
import termcolor


def seq_ping():
    print("Ok")

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1

    return gene_dict


def seq_reverse(seq):

    seq_inv = seq[::-1]

    return seq_inv


def seq_complement(seq):
    seq_dicc = {"A": "T", "C": "G", "G": "C", "T": "A"}
    complementary = ""
    for i in range(0, len(seq)):
        unit = seq[i]
        complementary += seq_dicc[unit]

    return complementary


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
            print("New sequence created!")

        else:
            self.strbases = "Error"
            print("INCORRECT Sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0,len(list_sequences)):
            text = "Sequence" + str(i) + ": (lenght:" + str(list_sequences[i].len()) + ")" + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def generate_seqs(pattern, number):
    #A, 3
    list_seq = []
    for i in range(0, number):
        #A   i = 0 ---- A
        #A   i = 1 -----AA
        #A   i = 2 -----AAA
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

