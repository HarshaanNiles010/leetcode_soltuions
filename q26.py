from typing import List 
# yeah forgot to mention this question sucks ass, the like to dislike ratio is through the roof and the question is poorly worded
# Развалюха 死ねえ
# no I am not going to put the translations for these words
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
