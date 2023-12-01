from typing import List

def longestPrefix(strs:[list[str]]) -> str:
    s = ""
    l = len(min(strs, key = len))
    strs.sort()
    for i in range(l):
        if strs[0][i] == strs[-1][i]:
            s += strs[0][i]
        else:
            break
    return s


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestPrefix(strs))