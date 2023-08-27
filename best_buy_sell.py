from typing import List

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