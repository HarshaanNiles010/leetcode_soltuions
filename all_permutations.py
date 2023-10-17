from typing import List
import itertools
# this just uses the itertools to generate all permutations of the list given 
# sooner than later a version which does this without some inbuilt function will be given
def permu(nums:List[int]) -> List[List[int]]:
    
    t = list(itertools.permutations(nums))
    r = []
    for i in t:
        r.append(list(i))
    return r
    
if __name__ == '__main__':
    nums = [1,2,3]
    print(permu(nums))
