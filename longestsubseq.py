from typing import List
def lengthLCS(s:str) -> int:
    s_set = set(s)
    length = 1
    for i in s:
        if i not in s_set:
            length += 1
    return length

if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthLCS(s))