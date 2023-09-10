from typing import List

def isValidPara(s:str) -> bool:
    """ closer = {
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
    
    print(True)  """
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()
    return not stack

if __name__ == '__mian__':
    s = "(]"
    print(isValidPara(s))