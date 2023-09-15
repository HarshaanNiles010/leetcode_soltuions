import re
def isPalindrome(s:str) -> bool:
    s = re.sub(r'[\W_]+', '', s)
    s = s.lower()
    return s == s[::-1]

if __name__ == '__main__':
    s = "ab_a"
    print(isPalindrome(s))
# Random Bull shit go
