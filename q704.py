from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    target = 4
    print(binarySearch(nums, target))