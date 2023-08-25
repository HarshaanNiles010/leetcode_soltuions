from typing import List

def sortedTwoSum(nums:List[int], target:int) -> List[int]:
    lptr = 0
    rptr = len(nums) - 1
    while lptr < rptr:
        if nums[lptr] + nums[rptr] == target:
            return [lptr+1,rptr+1]
        elif nums[lptr] + nums[rptr] > target:
            rptr = rptr - 1
        elif nums[lptr] + nums[rptr] < target:
            lptr = lptr + 1
            

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(sortedTwoSum(nums,target))