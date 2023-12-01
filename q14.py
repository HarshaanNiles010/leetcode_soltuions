from typing import List

def longestPrefix(strs:[list[str]]) -> str:
    s = ""
    l = len(min(strs, key = len))
    strs.sort()
    


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestPrefix(strs))