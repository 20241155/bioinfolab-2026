# lab10 데이터 출처표 (rbcL, 식물 8종)

확인일: 2026-11-04 · 출처: NCBI GenBank (nucleotide)

| 파일 | VERSION | ORGANISM | 길이 | 확인 방법 | 문제 |
|---|---|---|---|---|---|
| rbcL_arabidopsis.fa / .gb | OK432498.1 | Arabidopsis thaliana | 1440 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1440 bp 일치, `>` 1개 | **UNVERIFIED** 등록 서열이며 "rbcL-like" 유전자, partial |
| rbcL_fern.fa / .gb | MW620303.1 | Adiantum capillus-veneris | 1308 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1308 bp 일치, `>` 1개 | partial cds |
| rbcL_ginkgo.fa / .gb | KF221173.1 | Ginkgo biloba | 1317 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1317 bp 일치, `>` 1개 | partial cds |
| rbcL_ginseng.fa / .gb | HM142229.1 | Panax ginseng | 915 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 915 bp 일치, `>` 1개 | partial cds, 다른 종보다 훨씬 짧음(915 bp) → 정렬 시 비교 구간 줄어듦 |
| rbcL_liverwort.fa / .gb | LC536762.1 | Marchantia polymorpha subsp. ruderalis | 1399 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1399 bp 일치, `>` 1개 | partial cds, 아종(subsp.) 단위 |
| rbcL_maize.fa / .gb | Z11973.1 | Zea mays | 1431 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1431 bp 일치, `>` 1개 | DEFINITION에 complete/partial 표기 없음(오래된 항목) |
| rbcL_pine.fa / .gb | JQ512595.1 | Pinus thunbergii | 1428 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1428 bp 일치, `>` 1개 | 없음 (complete cds) |
| rbcL_rice.fa / .gb | L24073.1 | Oryza sativa | 1355 bp | grep VERSION/ORGANISM, fasta.py 길이 = LOCUS 1355 bp 일치, `>` 1개 | 분자 유형이 **mRNA** (나머지는 genomic DNA), LOCUS 이름이 RICCHRBCLA로 accession과 다름 |