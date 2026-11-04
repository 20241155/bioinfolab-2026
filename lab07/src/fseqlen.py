def length_print(seq):
    print(len(seq))
 
def length_return(seq):
    return len(seq)

a = length_print("ATGC")
b = length_return("ATGC")
 
print("a =", a)
print("b =", b)

def gc_content(seq):
    """서열의 GC 비율을 0과 1 사이의 수로 돌려준다."""
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)
