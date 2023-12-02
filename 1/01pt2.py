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

with open("input1.txt", "rt") as f:
    input_list = f.readlines()


def convert_to_digit(num):
    if num in num_map.keys():
        return int(num_map[num])
    return int(num)


total = 0

for line in input_list:
    num_first = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)[0]
    num_last = re.findall(
        r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1]
    )[0]

    total += convert_to_digit(num_first) * 10 + convert_to_digit(num_last[::-1])

print(total)
