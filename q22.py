from typing import List
# This is a backtracking question asking to generate all possible combinations with
# a certain number of pairs of paranthesis provided
# The basic concept keep the track of the open and close brackets throughout the algorithm

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
