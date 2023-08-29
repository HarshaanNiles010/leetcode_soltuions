
def rev(x:int) -> int:
    sign = [1,-1][x < 0]
    x = sign * int(str(abs(x))[::-1])
    return x if -(2**31)-1 < x < 2**31 else 0


if __name__ == '__main__':
    x = 1534236469
    print(rev(x))