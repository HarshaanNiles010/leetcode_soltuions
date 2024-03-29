from typing import List

def subsetWithDup(nums:List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def dfs(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return
        # All subsets that include nums[i]
        subset.append(nums[i])
        dfs(i + 1, subset)
        subset.pop()
        # All subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1, subset)

    dfs(0, [])
    return res   

if __name__ == '__main__':
    nums = [1,2,2]
    print(subsetWithDup(nums))