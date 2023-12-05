with open("D:\\Documents\\GitHub\\advent-of-code-2023\\3\\input3.txt") as f:
    lines = f.readlines()

# a boolean list of lists for tracking what we have found
global checked
checked = [[False for i in range(len(lines[0]))] for j in range(len(lines))]


def get_number(row, column):
    if checked[row][column]:
        return 0

    line = lines[row]
    number = line[column]
    start = column

    # get digits to the write
    index = start + 1
    while line[index].isdigit():
        number += line[index]
        index += 1

    # get digits to the left
    index = start - 1
    while line[index].isdigit():
        number = line[index] + number
        index -= 1

    # farthest left index
    starting = index + 1

    # mark it as counted, so we don't double count
    for i in range(starting, starting + len(number)):
        checked[row][i] = True

    return int(number)


GEAR_SYMBOL = "*"
INVALID_GEAR_LENGTH = 3
total = 0

for i, row in enumerate(lines):
    row = row.replace("\n", "")
    for j, char in enumerate(row):
        if char == GEAR_SYMBOL:
            checked = [[False for i in range(len(lines[0]))] for j in range(len(lines))]
            ls = []
            # bottom row
            if lines[i - 1][j].isdigit():
                ls.append(get_number(i - 1, j))
            if len(ls) <= INVALID_GEAR_LENGTH and lines[i - 1][j + 1].isdigit():
                ls.append(get_number(i - 1, j + 1))
            if len(ls) <= INVALID_GEAR_LENGTH and lines[i - 1][j - 1].isdigit():
                ls.append(get_number(i - 1, j - 1))

            # top row
            if len(ls) <= INVALID_GEAR_LENGTH and lines[i + 1][j].isdigit():
                ls.append(get_number(i + 1, j))
            if len(ls) <= INVALID_GEAR_LENGTH and lines[i + 1][j + 1].isdigit():
                ls.append(get_number(i + 1, j + 1))
            if len(ls) <= INVALID_GEAR_LENGTH and lines[i + 1][j - 1].isdigit():
                ls.append(get_number(i + 1, j - 1))

            if len(ls) <= INVALID_GEAR_LENGTH and lines[i][j + 1].isdigit():
                ls.append(get_number(i, j + 1))
            if len(ls) <= INVALID_GEAR_LENGTH and lines[i][j - 1].isdigit():
                ls.append(get_number(i, j - 1))

            ls = list(filter(lambda a: a != 0, ls))
            if ls is not None and len(ls) == 2:
                total += ls[0] * ls[1]

print(total)
