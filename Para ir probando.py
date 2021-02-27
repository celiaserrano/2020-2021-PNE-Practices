from statistics import mode
x = [0, 1, 2, 3, 4, 6, 6, 17, 16, 9, 10, 23, 12, 13, 14, 15, 16, 17, 18, 4, 20, 4, 22, 23, 24, 4, 4]
print(mode(x))




U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
sequence = U5_Seq[0:20]
print("Gene", ID, ":" )
print("Frag : ", sequence)
print("Comp : " , Seq0.seq_complement(sequence))




U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
sequence = U5_Seq[0:20]
print("Gene", ID, ":" )
print("Frag : ", sequence)
print("Rev : " , Seq0.seq_reverse(sequence))