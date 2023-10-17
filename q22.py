from typing import List


def valid_gen(s:str, n: int) -> bool:
    net_sum = 0
    for i in s:
        net_sum += ord(i)
    n = n * (ord("(") + ord(")"))
    if n == net_sum:
        return True
    return False

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