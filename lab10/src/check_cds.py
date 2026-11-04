import sys
from pathlib import Path
from Bio import SeqIO

# 기본값: 이 스크립트 기준 ../data
data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / "data"

print("file\tversion\torganism\tcds_location\tmatch")

for path in sorted(data_dir.glob("rbcL_*.gb")):
    rec = SeqIO.read(path, "genbank")
    version = rec.id                                  # VERSION (예: OK432498.1)
    organism = rec.annotations.get("organism", "NA")  # ORGANISM

    cds_list = [f for f in rec.features if f.type == "CDS"]
    if not cds_list:
        print(f"{path.name}\t{version}\t{organism}\tNA\tNO_CDS")
        continue

    for cds in cds_list:
        nt = cds.extract(rec.seq)
        # /codon_start 반영 (부분 CDS 는 2, 3 일 수 있음)
        start = int(cds.qualifiers.get("codon_start", ["1"])[0]) - 1
        nt = nt[start:]
        nt = nt[: len(nt) // 3 * 3]                   # 3의 배수로 자르기
        protein = str(nt.translate(table=11)).rstrip("*")  # 끝의 종결코돈 제거

        if "translation" in cds.qualifiers:
            match = protein == cds.qualifiers["translation"][0]
        else:
            match = "NO_TRANSLATION"

        print(f"{path.name}\t{version}\t{organism}\t{cds.location}\t{match}")
