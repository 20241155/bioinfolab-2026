import sys

def parse_gff(filepath):
    records = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if line.startswith(">"):      # FASTA 구간 시작 시 중단
                break
            fields = line.split("\t")
            if len(fields) < 9:
                continue
            seqid, source, feature, start, end, score, strand, phase, attributes = fields
            records.append({
                "seqid":      seqid,
                "feature":    feature,
                "start":      int(start),
                "end":        int(end),
                "strand":     strand,
                "attributes": attributes,
            })
    return records

def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "doc/prokka_out/sample.gff"
    records = parse_gff(filepath)

    # 1. CDS만 필터링
    cds_list = [r for r in records if r["feature"] == "CDS"]

    # 2. 길이 계산
    for r in cds_list:
        r["length"] = r["end"] - r["start"] + 1
    lengths = [r["length"] for r in cds_list]

    # 3. 통계
    print("=" * 50)
    print("CDS 통계")
    print("=" * 50)
    print(f"개수      : {len(cds_list)}")
    print(f"평균 길이 : {sum(lengths) / len(lengths):.1f} bp")
    print(f"최소 길이 : {min(lengths)} bp")
    print(f"최대 길이 : {max(lengths)} bp")

    # 4. 방향별 개수
    plus  = sum(1 for r in cds_list if r["strand"] == "+")
    minus = sum(1 for r in cds_list if r["strand"] == "-")
    print()
    print("방향별 개수")
    print("-" * 30)
    print(f"정방향 (+) : {plus}")
    print(f"역방향 (-) : {minus}")

    # 5. 가장 긴 CDS 5개
    top5 = sorted(cds_list, key=lambda r: r["length"], reverse=True)[:5]
    print()
    print("가장 긴 CDS 5개")
    print("-" * 50)
    for i, r in enumerate(top5, 1):
        print(f"[{i}] {r['seqid']}  {r['start']}–{r['end']}  ({r['strand']})  길이: {r['length']} bp")
        print(f"     {r['attributes']}")

if __name__ == "__main__":
    main()
    print(f"길이 합계 : {sum(lengths)} bp")
    print(f"코딩 밀도 : {sum(lengths) / 180912 * 100:.1f} %")