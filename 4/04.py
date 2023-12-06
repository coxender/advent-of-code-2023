with open("D:\\Documents\\GitHub\\advent-of-code-2023\\4\\input4.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

total = 0
for line in lines:
    scratch, winning = line.split("|")
    _, numbers = scratch.split(":")

    scratch_list = numbers.split(" ")
    winning_list = winning.split(" ")

    game_total = 0

    for num in scratch_list:
        if num.strip() == "":
            continue
        if num in winning_list:
            game_total = 1 if game_total == 0 else game_total * 2
    total += game_total
print(total)
