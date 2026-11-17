import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))
    return records

def mean_quality(qual):
    scores = [ord(ch) - 33 for ch in qual]
    return sum(scores) / len(scores)

filename = sys.argv[1]
reads = read_fastq(filename)

lengths = [len(seq) for _, seq, _ in reads]
quals   = [mean_quality(qual) for _, _, qual in reads]

print(f"read 개수: {len(reads)}")
print(f"평균 read 길이: {sum(lengths)/len(lengths):.2f}")
print(f"전체 평균 품질: {sum(quals)/len(quals):.4f}")
print(f"가장 짧은 read: {min(lengths)}")
print(f"가장 긴 read:   {max(lengths)}")