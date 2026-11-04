def gc_content(seq):
    """FASTA 파일을 읽어 {이름: 서열} 딕셔너리로 돌려준다."""
    return seq.count("G") / len(seq)

print는 화면에만 보여주고, return은 값을 돌려줘서 다시 쓸 수 있다. 

from fasta import read_fasta, gc_content

모듈로 import 되지 않고 직접 실행할 때만 작동하는 코드를 넣을 때 사용한다

w는 기존내용을 삭제하고 새로운 내용을 쓰고 a는 기존 내용 뒤에 이어쓴다.

오늘 겪은 오류 두가지
   1. 함수를 if __name__ 블록 아래 정의했다.
   2. KeyError: None 헤더 전에 서열 줄을 읽 발생하였다.