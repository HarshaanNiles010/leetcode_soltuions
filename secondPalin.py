def validPalindrome(s: str) -> bool:
    if s == s[::-1]: return True
    for i in range(len(s)):
        temp = s[:i] + s[i + 1:]
        if temp == temp[::-1]:
            return True
    return False

if __name__ == '__main__':
    s = "racssecar"
    print(validPalindrome(s))