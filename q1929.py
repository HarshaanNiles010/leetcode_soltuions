from typing import List 

def arrConcat(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * (2* n)
    for i in range(2*n):
        res[i] = nums[i%n]
    return res

if __name__ == '__main__':
    nums = [1,2,1]
    print(arrConcat(nums))

    