#!/usr/bin/bash
# batchinfo.sh — 폴더 안 모든 FASTA 파일의 서열 개수를 탭 표로 출력한다
# 사용법: batchinfo.sh <폴더>

if [ -z "$1" ]
then
    echo "사용법: $0 <폴더>"
    exit 1
fi

if [ ! -d "$1" ]
then
    echo "오류: 폴더를 찾을 수 없습니다: $1"
    exit 1
fi

DIR="$1"

if ! ls "$DIR"/*.fasta > /dev/null 2>&1
then
    echo "오류: FASTA 파일이 없습니다: $DIR"
    exit 1
fi

echo -e "file\tcount"
for F in "$DIR"/*.fasta
do
    echo -e "$(basename "$F")\t$(grep -c ">" "$F")"
done