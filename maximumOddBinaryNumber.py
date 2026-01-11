from collections import defaultdict
def maxOddBinaryNumber(s: str) -> str:
    nums = defaultdict(int)
    for c in s:
        nums[c] += 1
    temp = ["1"]*nums["1"] + ["0"]*nums["0"]
    res = "".join(temp[1:]) + temp[0]
    return res

if __name__ == '__main__':
    s = "100"
    print(maxOddBinaryNumber(s))