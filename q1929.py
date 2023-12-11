from typing import List 
# This problem can be summarized as replicate the original array and then paste it at the end. 
# Yeah it takes constant time but that's all
def arrConcat(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * (2* n)
    for i in range(2*n):
        res[i] = nums[i%n]
    return res

if __name__ == '__main__':
    nums = [1,2,1]
    print(arrConcat(nums))

    
