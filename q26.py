from typing import List 

def removeDuplicate(nums:List[int]) -> int:
    r = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[r] = nums[i]
            r += 1
    return r

if __name__ == '__main__':
    nums = [1,2,2]
    print(removeDuplicate(nums))