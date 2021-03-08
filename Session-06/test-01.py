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


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass


# --- Main program
s1 = Seq("AGTACACTGGT")   #can access all the mthods of the class //// instanciate the class so the methods no tienen por que estar ordenados
g = Gene("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Gene: {g}")
print(f"  Length: {g.len()}")