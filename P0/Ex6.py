import Seq0


GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-------| Exercice 6 | -------")

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    short_sequence = sequence[0:20]
    print("Gene",gene, ":")
    print("Frag : ", short_sequence)
    print("Rev:", Seq0.seq_reverse(short_sequence))


