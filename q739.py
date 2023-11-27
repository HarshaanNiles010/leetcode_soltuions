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
def dailyTemp(temp:List[int]) -> List[int]:
    pass


if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemp(temperatures))