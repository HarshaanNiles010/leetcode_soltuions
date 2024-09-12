from typing import List
import itertools



def letter_combinations(digits: str):
    if digits == "":
        return []
    
    digit_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    digits = list(digits)
    # declare an empty list used to fill with all the required lists whose combination is required
    t = []
    # fill the temporary list with charachter lists associated with a certain digit
    for digit in digits:
        t.append(digit_map[digit])
    # using itertools to easily find all the combinations that are required.
    t = list(itertools.product(*t))
    r = []
    # Iterools returns a list of tuples which further needed to combined to produce the desired results
    for i in t:
    # using the joing to append the results into a result List
        r.append("".join(i))
    return r




if __name__ == '__main__':
    digits = ""
    print(letter_combinations(digits))