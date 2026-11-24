import sys

def calc_n50(lengths):
    lengths_sorted = sorted(lengths, reverse=True)
    total = sum(lengths_sorted)
    half = total / 2
    
    cumsum = 0
    for length in lengths_sorted:
        cumsum += length
        if cumsum >= half:
            return length

def parse_fasta(filepath):
    lengths = []
    current_len = 0
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_len > 0:
                    lengths.append(current_len)
                current_len = 0
            else:
                current_len += len(line)
        if current_len > 0:
            lengths.append(current_len)
    return lengths

# FASTA 파일 읽기
fasta_file = sys.argv[1]
lengths = parse_fasta(fasta_file)

# 내림차순 정렬
lengths_sorted = sorted(lengths, reverse=True)

# N50 계산 및 출력
n50 = calc_n50(lengths)
print(f"contig 개수: {len(lengths_sorted)}")
print(f"전체 길이: {sum(lengths_sorted)}")
print(f"가장 긴 contig: {lengths_sorted[0]}")
print(f"N50: {n50}")

# doc/contig_lengths.txt 저장
output_path = "doc/contig_lengths.txt"
with open(output_path, "w") as f:
    for length in lengths_sorted:
        f.write(f"{length}\n")

print(f"\n'{output_path}' 파일에 저장 완료")