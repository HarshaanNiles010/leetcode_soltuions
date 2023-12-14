from typing import List
# yeah this question threw me off a bit but still we use the same idea of two pointers and try to put two pointers
def threeClosest(nums: List[int], target: int) -> int:
    tempSum = 0
    nums.sort()
    closest = 9999999999999999999999999999999
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            tempSum = nums[i] + nums[l] + nums[r]
            if tempSum < target:
                l += 1
            else:
                r -= 1
            if abs(tempSum - target) > abs(closest - target):
                closest = tempSum
    return closest

if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print(threeClosest(nums,target))
