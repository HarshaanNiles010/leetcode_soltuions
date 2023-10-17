from typing import List


def generate(n:int) -> List[str]:
    
    stack = []
    res = []
    def bactrack(openN: int, closeN: int):
        if openN == closeN == n:
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            bactrack(openN + 1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            bactrack(openN, closeN + 1)
            stack.pop()
    bactrack(0,0)
    return res
    
    

if __name__ == '__main__':
    n = 3
    s = "()()()"
    print(generate(n))