import Seq0


GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
for gene in gene_list:
    seque = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    seqq = seque[0:20]
    print("Gene", gene, ":", Seq0.seq_reverse(seqq))

for i in seq:
    if i == "A":
        x = "T"

    elif i == "C":
        x = "G"

    elif i == "G":
        x = "C"

    elif i == "T":
        x = "A"

    print("ola")

seq = ["A", "C", "A", "A", "T", "G", "G"]
gene_dict = {"A", "C", "G", "T"}
for d in seq:
    if gene_dict[d] == "A":
        d = "T"

print(gene_dict)