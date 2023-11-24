def hammingWeight(n:int) -> int:
    count = 0
    x = 1
    while n > 0:
        n &= n - 1
        count += 1
    return count 

if __name__ == '__main__':
    x = 1011
    print(hammingWeight(x))