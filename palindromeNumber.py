def palNumber(x:int) -> bool:
    if x < 0:
        return False
    return list(str(x)) == list(str(x))[::-1]


if __name__ == '__main__':
    x = 101
    print(palNumber(x))

# Random Bull shit go
