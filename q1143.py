from typing import List

def lcsLength(text1: str, text2: str) -> int:
    L = [[None]*(self.lengthListB + 1) for i in range(self.lengthListA + 1)] 
        for i in range(self.lengthListA + 1 ):
            for j in range(self.lengthListB + 1 ):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif self.numsListA[i - 1] == self.numsListB[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        self.lcsLength = L[self.lengthListA][self.lengthListB]

if __name__ == '__main__':
    
    text1 = "abcde"
    text2 = "ace" 
    print(lcsLength(text1, text2))