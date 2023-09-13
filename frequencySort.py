from typing import List
# okay this is not the most refined method to solve this problem but I didn't know any better at the moment
# so cut me some slack but yes a more upgraded method shall be updated as soon as I make it but mostly it shortens creation of the frequency table
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
