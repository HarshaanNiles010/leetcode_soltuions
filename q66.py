from typing import List

def plusOne(digits: List[int]) -> List[int]:
    temp = 0
    res = []
    for i in range(len(digits)):
        temp += digits[i] * (10 ** (len(digits) - i - 1))
    temp += 1
    while temp > 0:
        res.append(temp % 10)
        temp = temp // 10
    return res[::-1]

if __name__ == '__main__':
    digits = [1,2,3]
    print(plusOne(digits))
    