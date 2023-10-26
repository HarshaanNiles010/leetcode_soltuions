def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    t = list(t)
    s = list(s)
    stack = []
    for i in range(len(s)):
        if s[i] in t:
            stack.append(i)
        continue
    len_t = len(t)
    for i in range(len(stack)):
        pass
        
if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s,t))