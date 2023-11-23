from typing import List


def findDuplicate(nums: List[int]) -> int:
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count