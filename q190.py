def reverseBits(n: int) -> int:
    new_num = 0
    for i in range(32):
        bit = (n >> i) & 1
        new_num += (bit << (31 - i))
    return new_num

# yeah the people over leetcode decided you shall not take an input so here I am 
# No but in reality they just decided that the input is an int but the question says it's a string I spent like 35 min on just resolving that 
# So yeah couldn't care less Anyway fuck it