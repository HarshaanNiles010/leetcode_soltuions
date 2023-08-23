from typing import List
import collections

def groupAnagrams(strs:List[str]) -> List[List[str]]:
    result = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        result[tuple(count)].append(s)
    return result.values()
    

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))