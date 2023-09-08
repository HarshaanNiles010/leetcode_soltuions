
""" def getSum(s: str) -> int:
    t = 0
    for i in s:
        t += ord(i)
    return t



def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    t = 0
    for i in s1:
        t += ord(i)
    left = 0
    right = len(s1)
    for i in range(len(s2)):
        if t == getSum(s2[left + i: right + i]):
            return True
    return False """

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    left = 0
    right = len(s1)
    for i in range(len(s2)):
        if s1 == s2[left + i: right + i]:
            return True
    return False
        

if __name__ == '__main__':
    #s1 = "ab"
    #s2 = "eidbaooo"
    #print(checkInclusion(s1,s2))
    #s1 = "ab"
    #s2 = "eidboaoo"
    #print(checkInclusion(s1,s2))
    #s1 = "adc"
    #s2 = "dcda"
    #print(checkInclusion(s1,s2))
    s1 = "abc"
    s2 = "ccccbbbbaaaa"
    print(checkInclusion(s1,s2))