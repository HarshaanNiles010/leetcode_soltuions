from typing import List

""" def maxSlidingWindow(nums:List[int], k:int) -> List[int]:
    r = []
    for i in range(0,len(nums)):
        t = nums[i:i+k]
        if len(t) == k:
            r.append(max(t))
        else:
            continue
    return r """

def maxSlidingWindow(nums:List[int], k:int) -> List[int]:
    r = []
    t = nums[:k]
    r.append(max(t))
    for i in range(k,len(nums)):
        t.pop(0)
        t.append(nums[i])
        r.append(max(t))
    return r


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums,k))