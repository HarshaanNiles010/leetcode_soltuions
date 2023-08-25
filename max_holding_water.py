from typing import List

def maxArea(nums:List[int]) -> int:
    area = 1
    #This below is the naive approach to the problem
    '''for i in range(len(nums)):
        for j in range(len(nums)):
            if j - i < 0:
                area = max(-1*(j-i)*(min(nums[i],nums[j])), area)
            else:
                area = max((j-i)*(min(nums[i],nums[j])), area)
    return area'''
    pass

if __name__ == '__main__':
    nums = [1,8,6,2,5,4,8,3,7]
    print(maxArea(nums))