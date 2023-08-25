from typing import List

def LconseqSeq(nums:List[int]) -> int:
    numSet = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in numSet:
            length = 1
            while num in numSet:
                num += 1
                length += 1
                
        
        longest = max(length,longest) - 1

    return longest
    

if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(LconseqSeq(nums))