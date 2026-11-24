import sys

STOPS = ["TAA", "TAG", "TGA"]

def find_orfs(seq, frame):
    orfs = []
    start = None

    for i in range(frame, len(seq) - 2, 3):
        codon = seq[i:i + 3]

        if codon == "ATG" and start is None:
            start = i
        elif codon in STOPS and start is not None:
            orfs.append((start, i + 3))
            start = None

    return orfs

def reverse_complement(seq):
    complement = str.maketrans("ATCG", "TAGC")
    return seq.translate(complement)[::-1]

seq = sys.argv[1].upper()

print("=== 정방향 서열 ===")
for frame in [0, 1, 2]:
    orfs = find_orfs(seq, frame)
    print("틀", frame + 1, ":", orfs)
    for s, e in orfs:
        print("   ", seq[s:e], "길이", e - s)

rc_seq = reverse_complement(seq)
print("\n=== 역상보 서열 ===")
for frame in [0, 1, 2]:
    orfs = find_orfs(rc_seq, frame)
    print("틀", frame + 1, ":", orfs)
    for s, e in orfs:
        print("   ", rc_seq[s:e], "길이", e - s)
