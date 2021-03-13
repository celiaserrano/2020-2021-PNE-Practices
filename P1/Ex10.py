from Seq1 import Seq


PROJECT_PATH = "./project/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]


print("-----| Practice 1, Exercise 10 |------")


for gene in gene_list:
    s1 = Seq()
    sequence = s1.read_fasta(PROJECT_PATH + gene + ".txt")
    print("Gene", gene, ":", s1.most_freq_base())

