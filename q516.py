from typing import List

def lpsLength(s: str) -> int:
    L = [[None]*(len(s) + 1) for i in range(len(s) + 1)] 
    for i in range(len(s) + 1 ):
        for j in range(len(s) + 1 ):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s[i - 1] == s[::-1][j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    length = L[len(s)][len(s)]
    return length


if __name__ == '__main__':
    s = "bbbab"
    print(lpsLength(s))