from typing import List
# This problem can be solved with stack, put the current paranthesis into the stack
# and when it's other half is found throw it out of stack and if there is something 
# left in the stack then it is not a valid paranthesis otherwise it is.
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

if __name__ == '__main__':
    s = "(]"
    print(isValidPara(s))
