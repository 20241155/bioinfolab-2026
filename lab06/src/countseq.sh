n = 0
with open("lab06/data/seqs.fasta") as f:
    for line in f:
        if line.startswith(">"):
            n = n + 1
 
print(n)
