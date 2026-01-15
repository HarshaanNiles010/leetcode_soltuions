from typing import List

def maxProfit(prices: List[int]) -> int:
    left = 0
    right = 1
    maxP = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            maxP = max(maxP, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return maxP

if __name__ == '__main__':
    prices = [10,1,5,6,7,1]
    print(maxProfit(prices))