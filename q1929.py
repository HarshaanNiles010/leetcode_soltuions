from typing import List 

def arrConcat(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * (2* n)
    for i in range(n):
        res[i] = nums[i%n]
    return res



    