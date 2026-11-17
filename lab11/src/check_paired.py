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

def base_name(full_name):
    # 마지막 공백 기준으로 split 후 첫 번째 토큰에서
    # 마지막 .1 / .2 또는 /1 /2 제거
    token = full_name.split()[0]
    for suffix in ['.1', '.2', '/1', '/2']:
        if token.endswith(suffix):
            return token[:-len(suffix)]
    return token

file1 = sys.argv[1]
file2 = sys.argv[2]

reads1 = read_fastq(file1)
reads2 = read_fastq(file2)

print(f"파일 1 read 개수: {len(reads1)}")
print(f"파일 2 read 개수: {len(reads2)}")

if len(reads1) != len(reads2):
    print("❌ read 개수가 다릅니다!")
    sys.exit(1)
else:
    print("✅ read 개수 일치")

print()

mismatch = 0
for i, ((n1, _, _), (n2, _, _)) in enumerate(zip(reads1, reads2)):
    b1 = base_name(n1)
    b2 = base_name(n2)
    if b1 != b2:
        mismatch += 1
        if mismatch <= 5:
            print(f"❌ 불일치 (위치 {i+1}): {n1} vs {n2}")

if mismatch == 0:
    print(f"✅ 전체 {len(reads1)}개 read 이름 모두 짝 일치")
else:
    print(f"❌ 총 {mismatch}개 짝 불일치")