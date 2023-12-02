import re

total_score = 0
with open("input2.txt", "rt") as f:
    input_list = f.readlines()

for line in input_list:
    max_rgb = {"red": 0, "blue": 0, "green": 0}

    invalid = False
    split_line = re.split(":|;|,", line)
    split_line.pop(0)
    labeled_line = [list(tuple(re.split("\s", item.strip()))) for item in split_line]
    for pair in labeled_line:
        label = pair[1]
        cubes = int(pair[0])
        max_rgb[label] = max(max_rgb[label], cubes)
    total_score += max_rgb["red"] * max_rgb["blue"] * max_rgb["green"]

print(total_score)
