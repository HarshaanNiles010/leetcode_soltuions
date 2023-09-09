from typing import List



def RPN(tokens: List[str]) -> int:
    r = 0
    symbols = ["+","-","*","/"]
    result = []
    s = ""
    f""" or i in range(len(tokens)):
        if tokens[i] in symbols:
            s = tokens.pop(tokens.index(tokens[i]))
            t_0 = int(tokens.pop(tokens.index(tokens[i - 1])))
            #t_0 = int(tokens[i - 1])
            #t_1 = int(tokens.pop(tokens.index(tokens[i - 2])))
            t_1 = int(tokens[i - 2])
            if s == "+":
                r = t_0 + t_1
                tokens[i - 2] = str(r)
                #tokens.insert(str(r), tokens.index(tokens[i - 2]))
            elif s == "-":
                r = t_0 - t_1
                tokens[i - 2] = str(r)
                #tokens.insert(str(r), tokens.index(tokens[i - 2]))
            elif s == "*":
                r = t_0 * t_1
                tokens[i - 2] = str(r)
                #tokens.insert(str(r), tokens.index(tokens[i - 2]))
            elif s == "/":
                r = int(t_0/t_1)
                tokens[i - 2] = str(r)
                #tokens.insert(str(r), tokens.index(tokens[i - 2])) """
    """ i = 0
    while len(tokens) > 1:
        i += 1
        if tokens[i] in symbols:
            s = tokens.pop(tokens.index(tokens[i]))
            t_0 = int(tokens.pop(tokens.index(tokens[i - 1])))
            t_1 = int(tokens[i - 2])
            if s == "+":
                r = t_0 + t_1
                tokens[i - 2] = str(r)
                i = 0
            elif s == "-":
                r = t_0 - t_1
                tokens[i - 2] = str(r)
                i = 0
            elif s == "*":
                r = t_0 * t_1
                tokens[i - 2] = str(r)
                i = 0
            elif s == "/":
                r = int(t_1/t_0)
                tokens[i - 2] = str(r)
                i = 0
    return int(tokens[0]) """
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b) / a))
        else:
            stack.append(int(c))
    return stack[0]

if __name__ == '__main__':
    tokens = ["4","13","5","/","+"]
    print(RPN(tokens))
                