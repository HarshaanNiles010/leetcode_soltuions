import random 
import time
import string
from datetime import datetime, date

def generate_random_strings(length: int) -> str:
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_random_file(file_path: str, length: int):
    with open(file_path, 'w') as file:
        file.write(generate_random_strings(length))

def generate_file_path(current_direc: str) -> string:
    return current_direc + '/' + str(date.today()) + "" +random.choice(string.digits)+ random.choice(string.digits) + '.txt'

def chaos():
    print("May chaos take the world")
    current_direc = "/Users/harshaanbabra/Desktop/Code/Python/leetcode_soltuions"
    length = 10
    file_path = generate_file_path(current_direc)
    generate_random_file(file_path, length)
