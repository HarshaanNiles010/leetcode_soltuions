from typing import List

def maxArea(nums:List[int]) -> int:
    #This below is the naive approach to the problem
    '''for i in range(len(nums)):
        for j in range(len(nums)):
            if j - i < 0:
                area = max(-1*(j-i)*(min(nums[i],nums[j])), area)
            else:
                area = max((j-i)*(min(nums[i],nums[j])), area)
    return area'''
    
    l = 0
    r = len(nums) - 1
    area = 1
    while l < r:
        breadth = r - l
        width = min(nums[r],nums[l])
        area = max(breadth * width, area)
        if nums[l] < nums[r]:
            l += 1
        elif nums[r] <= nums[l]:
            r -= 1
    return area            


if __name__ == '__main__':
    nums = [1,8,6,2,5,4,8,3,7]
    print(maxArea(nums))

# Random Bull shit go
