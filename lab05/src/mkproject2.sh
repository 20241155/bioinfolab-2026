#!/usr/bin/bash
# mkproject2.sh — 프로젝트 폴더(data, doc, src)와 doc/README를 만든다.
# 사용법: mkproject2.sh <프로젝트이름>

if [ -z "$1" ]
then
    echo "사용법: $0 <프로젝트이름>"
    exit 1
fi

NAME="$1"

if [ -e "$NAME" ]
then
    echo "오류: 이미 존재합니다: $NAME"
    exit 1
fi

mkdir -p "$NAME"/data "$NAME"/doc "$NAME"/src
echo "프로젝트: $NAME" > "$NAME"/doc/README
echo "생성일: $(date)" >> "$NAME"/doc/README
echo "$NAME 프로젝트를 만들었습니다."
ls -R "$NAME"