def multiplyStrings(s1: str, s2:str) -> str:
    
    
    numsDict = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9
    }
    strDict = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
    }
    s1 = list(s1)
    s2 = list(s2)
    s1_num = []
    s2_num = []
    num_1 = 0
    num_2 = 0
    res = []
    for c in s1:
        s1_num.append(numsDict[c])
    for c in s2:
        s2_num.append(numsDict[c])
    for i in range(len(s1_num)):
        num_1 += s1_num[i]*(10 ** (len(s1_num) - i - 1))
    for i in range(len(s2_num)):
        num_2 += s2_num[i]*(10 ** (len(s2_num) - i - 1))
    if num_1 == 0:
        num_3 = num_2
    elif num_2 == 0:
        num_3 = num_1
    else:
        num_3 = num_2 * num_1
    while num_3 > 0:
        res.append(num_3%10)
        num_3 = num_3 // 10
    for i in range(len(res)):
        res[i] = strDict[res[i]]
    return "".join(res)[::-1]
    
    


if __name__ == '__main__':
    s1 = "2"
    s2 = "3"
    print(multiplyStrings(s1,s2))