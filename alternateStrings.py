def alterStrings(word1: str, word2: str) -> str:
    n = len(word1)
    m = len(word2)
    res = []
    i = 0
    j = 0
    while i < 0 or j < 0:
        if i < n:
            res.append(word1[i])
        if j < m:
            res.append(word2[j])
        i += 1
        j += 1
    return "".join(res)

if __name__ == '__main__':
    w1 = "abc"
    w2 = "pqr"
    result = alterStrings(w1, w2)
    print(result)  # Expected output: "apbqcr"