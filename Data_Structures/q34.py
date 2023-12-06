from typing import List 

def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1,-1]
    if target not in nums:
        return [-1,-1]
    first_left = 0
    first_right = len(nums) - 1
    res = []
    while first_left < first_right:
        if nums[first_left] < target:
            first_left += 1
        elif nums[first_right] > target:
            first_right -= 1
        else:
            res.append([first_left, first_right])
            break
    return res

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 6
    print(searchRange(nums,target))