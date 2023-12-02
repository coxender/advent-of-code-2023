import re

red_limit = 12
green_limit = 13
blue_limit = 14
invalid = False

total_valid = 0
with open("input2.txt", "rt") as f:
    input_list = f.readlines()

for line in input_list:
    invalid = False
    split_line = re.split(":|;|,", line)
    game = int(split_line.pop(0)[5:])
    for output in split_line:
        if "blue" in output:
            invalid = int(output[:-5]) > blue_limit
        elif "red" in output:
            invalid = int(output[:-4]) > red_limit
        elif "green" in output:
            invalid = int(output[:-6]) > green_limit

        if invalid:
            break
    total_valid += 0 if invalid else game

print(total_valid)
