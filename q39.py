from typing import List

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    dp = [[] for i in range(target + 1)]
    for c in nums:
        for i in range(c, target + 1):
            if i == c:
                dp[i].append([c])
            for comb in dp[i - c]:
                dp[i].append(comb + [c])
    return dp[-1]

if __name__ == '__main__':
    nums = [2,3,6,7]
    target = 7
    combination_sum(nums, target)