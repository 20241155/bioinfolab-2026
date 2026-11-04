#!/usr/bin/bash
# fastainfo.sh — FASTA 파일의 정보를 출력한다
# 사용법: fastainfo.sh <FASTA파일>

if [ -z "$1" ]
then
    echo "사용법: $0 <FASTA파일>"
    exit 1
fi

if [ ! -f "$1" ]
then
    echo "오류: 파일을 찾을 수 없습니다: $1"
    exit 1
fi

FILE="$1"

echo "파일: $FILE"
echo "서열 개수:"
grep -c ">" "$FILE"
echo "서열 이름:"
grep ">" "$FILE" | cut -d" " -f1 | cut -c2-
echo "총 염기 수(대략):"
grep -v ">" "$FILE" | tr -d "\n" | wc -m