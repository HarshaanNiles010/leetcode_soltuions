# yeah I hate how I have a perfectly working answer better in readability then this peice of shit here but yeah this is somehow working even when mine wasn't 
# so I just added my code in the comments
# I hope it helps
'''
def rev(x:int) -> int:
    MAX_NUM = 2**31
    if x >= (MAX_NUM - 1) or x <= (-1)*(MAX_NUM):
        return 0
    if x < 0:
        x = x * -1
        x = list(str(x))[::-1]
        x = int(''.join(x))
        x = x * -1
        return x
    x = list(str(x))[::-1]
    x = int(''.join(x))
    return x
'''
def rev(x:int) -> int:
    sign = [1,-1][x < 0]
    x = sign * int(str(abs(x))[::-1])
    return x if -(2**31)-1 < x < 2**31 else 0


if __name__ == '__main__':
    x = 1534236469
    print(rev(x))
