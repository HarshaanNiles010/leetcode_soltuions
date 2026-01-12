
from collections import defaultdict


def indexFirstUnique(s: str) -> int:
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    for i, c in enumerate(s):
        if count[c] == 1: return i
    return -1

if __name__ == '__main__':
    s: str = "baab"
    print(indexFirstUnique(s))