from typing import List 

""" def dailyTemp(temp: List[int]) -> List[int]:
    res = [0] * len(temp)
    newStack = []
    for i, j in enumerate(temp):
        while newStack and j > newStack[-1][0]:
            temperature, index = newStack.pop()
            res[index] = i - index
        newStack.append((j,i))
    return res
"""
# This algorithm has a small problem this one doesn't account for when the temperature increases but then has an increasing sequence below
# The peak
def dailyTemp(temp:List[int]) -> List[int]:
    leftPtr = 0
    rightPtr = 0
    res = []
    while rightPtr < len(temp) and leftPtr < len(temp):
        if temp[leftPtr] < temp[rightPtr]:
            res.append(rightPtr - leftPtr)
            leftPtr += 1
            rightPtr = leftPtr
        else:
            rightPtr += 1
    shortFall = [0] * (len(temp) - len(res))
    res = res + shortFall
    return res


if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemp(temperatures))
    temperatures = [30,40,50,60]
    print(dailyTemp(temperatures))