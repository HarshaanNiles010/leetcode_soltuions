from typing import List

def lcsLength(text1: str, text2: str) -> int:
    L = [[None]*(len(text2) + 1) for i in range(len(text1) + 1)] 
    for i in range(len(text1) + 1 ):
        for j in range(len(text2) + 1 ):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    length = L[text1][text2]
    return length

if __name__ == '__main__':
    
    text1 = "abcde"
    text2 = "ace" 
    print(lcsLength(text1, text2))