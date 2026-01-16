def tribon(n: int) -> int:
    temp = [0] * (n + 1)
    temp[0] = 0
    temp[1] = 1
    temp[2] = 1
    for i in range(3, n + 1):
        temp[i] = temp[i - 1] + temp[i - 2] + temp[i - 3]
    return temp[len(temp) - 1]

if __name__ == '__main__':
    n = 21
    print(tribon(n))