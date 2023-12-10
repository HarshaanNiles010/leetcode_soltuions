def intToRoman(n:int) -> str:
    # This is a question where having a lookup table of all the possible combinations makes it easier to compute the solution.
    # On the other hand there exsits a solution under which the current roman numeral is subtracted to find it's actual value or sth
    # Creating Dictionary for Lookup
    num_map = {
        1: "I",
        5: "V",    4: "IV",
        10: "X",   9: "IX",
        50: "L",   40: "XL",
        100: "C",  90: "XC",
        500: "D",  400: "CD",
        1000: "M", 900: "CM",
    }
        
        # Result Variable
    r = ''
        
        
    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        # If n in list then add the roman value to result variable
        while n <= num:
            r += num_map[n]
            num-=n
    return r


if __name__ == '__main__':
    num = 3
    print(intToRoman(num))
