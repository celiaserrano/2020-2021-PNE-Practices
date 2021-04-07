import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases = NULL_SEQUENCE):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases = strbases

        else:

            if self.is_valid_sequence():
                print("New sequence created!")

            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0,len(list_sequences)):
            text = "Sequence" + str(i) + ": (lenght:" + str(list_sequences[i].len()) + ") " + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0

        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
          for ch in self.strbases:
            if ch == "A":
                a += 1
            elif ch == "C":
                c += 1
            elif ch == "G":
                g += 1
            else:
                t += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A":a, "C":c, "G":g, "T":t}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]


    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif "T":
                    complement += "A"

            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")



    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())


    def most_freq_base(self):
        a, c, g, t = self.count_bases()
        if a > c and a > g and a > t:
            return "Most frequent Base: A"

        elif c > a and c > g and c > t:
            return "Most frequent Base: C"

        elif g > a and g > c and g > t:
            return "Most frequent Base: G"

        else:
            return "Most frequent Base: T"




def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid Sequence")
    return s1, s2, s3
