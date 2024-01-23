from typing import List

def subsetWithDup(nums:List[int]) -> List[List[int]]:
    res = []
    subset = []
    i = len(nums) - 1
    def dfs(i):
        if i < 0:
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i - 1)
        nums.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i - 1)
    dfs(i)
    return res    

if __name__ == '__main__':
    nums = [1,2,2]
    print(subsetWithDup(nums))