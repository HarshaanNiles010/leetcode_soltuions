def reverseBits(n: int) -> int:
    new_num = 0
    for i in range(32):
        bit = (n >> i) & 1
        new_num += (bit << (31 - i))
    return new_num

# yeah the people over leetcode decided you shall not take an input so here I am 