# The problem is find the  min length window whose sum is greater than or equal to a target
from typing import List 

def min_length_window(nums: List[int], target:int) -> int:
    min_length = float('inf')
    leftPtr = 0
    rightPtr = 0
    current_sum = 0
    while rightPtr < len(nums):
        current_sum += nums[rightPtr]
        rightPtr += 1
        while leftPtr < rightPtr and current_sum >= target:
            current_sum -= nums[leftPtr]
            leftPtr += 1
        min_length = min(min_length, rightPtr - leftPtr + 1)
    return min_length

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    target = 10
    print(min_length_window(nums, target))