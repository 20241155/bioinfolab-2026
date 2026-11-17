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

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return gc / len(seq) * 100

def mean_quality(qual):
    scores = [ord(ch) - 33 for ch in qual]
    return sum(scores) / len(scores)

reads = read_fastq(sys.argv[1])

results = []
for name, seq, qual in reads:
    gc = gc_content(seq)
    mq = mean_quality(qual)
    results.append((name, gc, mq))

# 전체 평균
total_gc = sum(r[1] for r in results) / len(results)
total_mq = sum(r[2] for r in results) / len(results)

print(f"전체 read 수: {len(results)}")
print(f"전체 평균 GC 비율: {total_gc:.4f}%")
print(f"전체 평균 품질:    {total_mq:.4f}")
print()

# GC 비율 기준 정렬
sorted_by_gc = sorted(results, key=lambda x: x[1])

# GC 낮은 상위 10개
low_gc = sorted_by_gc[:10]
# GC 높은 상위 10개
high_gc = sorted_by_gc[-10:]

print("=== GC 비율 낮은 read 10개 ===")
print("이름\tGC 비율(%)\t평균 품질")
for name, gc, mq in low_gc:
    print(f"{name}\t{gc:.4f}\t{mq:.4f}")
low_mq_mean = sum(r[2] for r in low_gc) / len(low_gc)
print(f"→ 평균 품질: {low_mq_mean:.4f}  (전체 평균과 차이: {low_mq_mean - total_mq:+.4f})")

print()

print("=== GC 비율 높은 read 10개 ===")
print("이름\tGC 비율(%)\t평균 품질")
for name, gc, mq in high_gc:
    print(f"{name}\t{gc:.4f}\t{mq:.4f}")
high_mq_mean = sum(r[2] for r in high_gc) / len(high_gc)
print(f"→ 평균 품질: {high_mq_mean:.4f}  (전체 평균과 차이: {high_mq_mean - total_mq:+.4f})")