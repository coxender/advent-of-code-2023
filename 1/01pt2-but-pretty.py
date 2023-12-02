import re

num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

regex_norm = "\d|" + "|".join(num_map.keys())
regex_oh_no = "\d|" + "|".join([key[::-1] for key in num_map.keys()])
total = 0


def convert_to_digit(num):
    if num in num_map.keys():
        return int(num_map[num])
    return int(num)


with open("input1.txt", "rt") as f:
    input_list = f.readlines()

for line in input_list:
    num_first = re.findall(regex_norm, line)[0]
    num_last = re.findall(regex_oh_no, line[::-1])[0]

    total += convert_to_digit(num_first) * 10 + convert_to_digit(num_last[::-1])

print(total)
