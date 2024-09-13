from typing import List


def searchInsert(nums: List[int], target: int):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l



if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target))