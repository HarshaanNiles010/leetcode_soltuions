from typing import List

# this is a two pointer problem where I used the first pointer to chose an element and then another while loop to sort out the rest of elements in that set 
def threeSum(nums:List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, j in enumerate(nums):
            # Skip positive integers
        if j > 0:
            break

        if i > 0 and j == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = j + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([j, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))
