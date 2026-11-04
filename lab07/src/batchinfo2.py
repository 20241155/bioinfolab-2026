import sys
import glob
from fasta import read_fasta, gc_content, length_stats

folder = sys.argv[1]
outfile = sys.argv[2]

with open(outfile, "w") as out:
    out.write("file\tcount\ttotal\tmean_gc\n")
    for path in sorted(glob.glob(folder + "/*.fasta")):
        seqs = read_fasta(path)
        stats = length_stats(seqs)
        avg_gc = sum(gc_content(s) for s in seqs.values()) / stats["count"]
        out.write(f"{path}\t{stats['count']}\t{stats['total']}\t{round(avg_gc, 3)}\n")

print("저장 완료:", outfile)