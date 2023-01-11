
import re

with open(r"D:\Advent of Code\2015\day5_input.txt", "r") as file:
    # read the contents of the file into a string
    strings = file.readlines()

# Got the below code from ChatGPT

def is_nice(string:str)->bool:
    
    # matches any string that contains at least 3 vowels
    return bool(re.search(r'(.*[aeiou].*){3,}', string) 

    # does not match any string that contains the substrings "ab", "cd", "pq", or "xy"
    and not re.search(r'ab|cd|pq|xy', string) 

    # matches any string that contains a letter that appears twice in a row
    and re.search(r'([a-z])\1', string))

nice_strings = 0

# Loop through the list of strings

for string in strings:

    if is_nice(string) == True:
        nice_strings += 1
    else:
        continue

print(nice_strings)