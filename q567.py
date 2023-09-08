from collections import Counter
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

""" def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    left = 0
    right = len(s1)
    for i in range(len(s2)):
        if s1 == s2[left + i: right + i]:
            return True
    return False """
def checkInclusion(s1: str, s2: str) -> bool:
    s1_map = Counter(s1)
    match = 0
        
    for i in range(len(s2)):
        # Add right
        if s2[i] in s1_map:
            s1_map[ s2[i] ] -= 1
            if s1_map[ s2[i] ] == 0: match += 1
            
            # Subtract left
        if i+1 > len(s1):
            if (left:=s2[i-len(s1)]) in s1_map:
                s1_map[left] += 1
                # means it came to 1 from 0
                if s1_map[ left ] == 1: match -= 1    
    if match == len(s1_map):
        return True
        

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