# This is the problem statement, 
# Get the sum of a window of length k
# you are given an array nums and you have to return the sum of elements in a particular window of length k


from typing import List

def static_window(nums: List[int], length: int) -> List[int]:
    # here length represents the window length required
    windowSum = sum(nums[:length])
    res = [windowSum]
    for i in range(1, len(nums) - length + 1):
        windowSum -= nums[i - 1]
        windowSum += nums[i + length - 1]
        res.append(windowSum)
    return res

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    length = 3
    print(static_window(nums, length))