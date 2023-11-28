def lengthOfLongestSubstring(s:str) -> int:
    charSet = set()
    start = 0
    max_length = 0
    for i in range(len(s)):
        while s[i] in charSet:
            charSet.remove(s[start])
            start += 1
        charSet.add(s[i])
        max_length = max(max_length, i - start + 1)
    return max_length

if __name__ == '__main__':
    #s = "bbbb"
    #print(lengthOfLongestSubstring(s))
    #s = "abcabcbb"
    #print(lengthOfLongestSubstring(s))
    s ="dvdf"
    print(lengthOfLongestSubstring(s))