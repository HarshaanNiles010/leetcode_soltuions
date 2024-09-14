from typing import List


def rob(nums:List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    




if __name__ == '__main__':
    nums = [2,3,2]