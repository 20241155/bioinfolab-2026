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

def qual_by_position(records):
    position_scores = {}

    for name, seq, qual in records:
        for i, ch in enumerate(qual):
            score = ord(ch) - 33
            if i not in position_scores:
                position_scores[i] = []
            position_scores[i].append(score)

    result = []
    for pos in sorted(position_scores.keys()):
        scores = position_scores[pos]
        mean = sum(scores) / len(scores)
        result.append((pos + 1, mean))  # 1-based position

    return result

reads = read_fastq(sys.argv[1])
position_means = qual_by_position(reads)

print("위치(bp)\t평균 품질")
for pos, mean in position_means:
    print(f"{pos}\t{mean:.4f}")