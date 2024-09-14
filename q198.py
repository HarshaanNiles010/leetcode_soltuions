from typing import List


def rob(nums:list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    temp = nums.copy()
    temp[1] = max(nums[0],nums[1])
    for i in range(2, len(nums)):
        temp[i] = max(temp[i - 1], nums[i] + temp[i - 2])
    return temp[len(nums) - 1]


if __name__ == '__main__':
    nums = [2,7,9,3,1]
    print(rob(nums))
    