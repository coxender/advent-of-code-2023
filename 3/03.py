with open("D:\\Documents\\GitHub\\advent-of-code-2023\\3\\input3.txt") as f:
    lines = f.readlines()

# a boolean list of lists for tracking what we have found
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


symbols = "!@#$%^&*()_+-=/"
total = 0

for i, row in enumerate(lines):
    for j, char in enumerate(row.replace("\n", "")):
        if char == ".":
            continue
        if char in symbols:
            # bottom row
            if lines[i - 1][j].isdigit():
                total += get_number(i - 1, j)
            if lines[i - 1][j + 1].isdigit():
                total += get_number(i - 1, j + 1)
            if lines[i - 1][j - 1].isdigit():
                total += get_number(i - 1, j - 1)

            # top row
            if lines[i + 1][j].isdigit():
                total += get_number(i + 1, j)
            if lines[i + 1][j + 1].isdigit():
                total += get_number(i + 1, j + 1)
            if lines[i + 1][j - 1].isdigit():
                total += get_number(i + 1, j - 1)

            if lines[i][j + 1].isdigit():
                total += get_number(i, j + 1)
            if lines[i][j - 1].isdigit():
                total += get_number(i, j - 1)

print(total)
