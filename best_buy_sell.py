from typing import List
# this is an example of the sliding window where you move the window to the point when you can sell the product
def max_profit(prices:List[int]) -> int:
    res = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res,price - lowest)
    return res

if __name__ == '__main__':
    prices=[7,1,5,3,6,4]
    print(max_profit(prices))
