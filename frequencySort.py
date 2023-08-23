from typing import List

def freqSort(s:str)->str:
    e = list(set(s))
    c = [0] * len(e)
    d = dict(zip(e,c))
    for c in s:
        d[c] += 1
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    nl = []
    for i in d:
        nl.append(i*d[i])
    n = ''.join(nl)
    return n
if __name__ == '__main__':
    s = "tree"
    print(freqSort(s))