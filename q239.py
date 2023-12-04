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
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums,k))