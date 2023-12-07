from typing import List

def moveZero(nums:List[int]) -> List[int]:
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[left] == 0:
            nums[left], nums[i] = nums[i], nums[left]
        if nums[left] != 0:
            left += 1
    return nums



if __name__ == '__main__':
    #nums = [0,1,0,3,12]
    #print(moveZero(nums))
    nums = [0,1]
    print(moveZero(nums))