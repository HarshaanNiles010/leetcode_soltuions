from typing import List

def isValidPara(s:str) -> bool:
    closer = {
        ')':'(',
        '}':'{',
        '[':']'
    }
    stack = []
    for c in s:
        if c not in closer:
            stack.append(c)
            continue
        if not stack or stack[-1] != closer[c]:
            print(False)
        stack.pop()
    
    print(True) 

if __name__ == '__mian__':
    s = "(]"
    print(isValidPara(s))