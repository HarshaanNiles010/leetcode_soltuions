from typing import List

def Product(nums:List[int]) -> List[int]:
    r = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        r[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        r[i] *= postfix
        postfix *= nums[i]
    
    return r
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Product(nums))