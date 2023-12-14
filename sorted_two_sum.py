from typing import List
# In this question since we know the array is sorted we can use two pointers yet again
# place one pointer at the start of the list and the other at the end of the list, then keep moving the left pointer if the total is less than the target
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
