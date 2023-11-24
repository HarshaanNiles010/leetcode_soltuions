from typing import List
def minSpeed(plates:List[int], h: int) -> int:
    l, r = 1, max(plates)
    res = r

    while l <= r:
        k = (l + r) // 2
        totalTime = 0
        for p in plates:
            totalTime += math.ceil(float(p) / k)
        if totalTime <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res

if __name__ == '__main__':
    plates = [3,6,7,11]
    h = 8
    print(minSpeed(plates,h))