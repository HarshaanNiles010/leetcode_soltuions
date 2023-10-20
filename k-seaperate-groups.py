from typing import List


# Check wehter the input list of numbers can be converted into k-groups of equal sum
# If a list has numbers like [1,2,3,6] then there can be two subgroups of sum 6 i.e [[1,2,3], [6]]
# we need to find out if there are k distinct sub groups of same sum or not 
# Another Example might be [1,2,3,4,6,8] -> [1,2,3,6],[4,8],[2,4,6],[1,3,8] 

# This question is an example of a bactracking algorithm

def k_groups(nums: List[int], k: int) -> bool:
    
    if sum(nums) % k != 0:
        return False
    
    nums.sort(reverse = True)
    target = sum(nums) / k
    visited = set()
    
    
    def backTrack(idx, count, currSum):
        if count == k:
            return True
        
        if target == currSum:
            return backTrack(0, count + 1, 0)
        
        for i in range(idx, len(nums)):
            if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                continue
            if i in visited or currSum + nums[i] > target:
                continue
            visited.add(i)
            if backTrack(i + 1, count, currSum + nums[i]):
                return True
            visited.remove(i)
        return False
    return backTrack(0,0,0)

if __name__ == '__main__':
    nums = [1,2,3,4,6,8]
    print(k_groups(nums,k=0))