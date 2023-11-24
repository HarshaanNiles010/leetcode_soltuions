from typing import List 

def findSingle(nums: List[int]) -> int:
    count = []
    for num in nums:
        if num not in count:
            count.append(num)
        else:
            count.pop(count.index(num))
    return count[0]


if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(findSingle(nums))