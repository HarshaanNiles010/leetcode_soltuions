from typing import List



def RPN(tokens: List[str]) -> int:
    r = 0
    symbols = ["+","-","*","/"]
    result = []
    s = ""
    for i in range(len(tokens)):
        if tokens[i] in symbols:
            s = tokens.pop(tokens.index(tokens[i]))
            t_0 = int(tokens.pop(tokens.index(tokens[i - 1])))
            t_1 = int(tokens.pop(tokens.index(tokens[i - 2])))
            if s == "+":
                r = t_0 + t_1
                tokens.insert(str(r), tokens.index(tokens[i - 2]))
            elif s == "-":
                r = t_0 - t_1
                tokens.insert(str(r), tokens.index(tokens[i - 2]))
            elif s == "*":
                r = t_0 * t_1
                tokens.insert(str(r), tokens.index(tokens[i - 2]))
            elif s == "/":
                r = int(t_0/t_1)
                tokens.insert(str(r), tokens.index(tokens[i - 2]))
    return int(tokens[0])

if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    print(RPN(tokens))
                