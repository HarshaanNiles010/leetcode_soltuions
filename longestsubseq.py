from typing import List
def lengthLCS(s:str) -> int:
    hash_set = set()
    length = 0
    result_length = 0
    for i in range(len(s)):
        while s[i] in hash_set:
            hash_set.remove(s[length])
            length += 1
        hash_set.add(s[i])
        result_length = max(result_length,i - length + 1)
    return result_length

if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthLCS(s))