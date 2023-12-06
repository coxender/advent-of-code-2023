with open("D:\\Documents\\GitHub\\advent-of-code-2023\\4\\input4.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

scratchcards = [1 for _ in range(len(lines))]

for line in lines:
    scratch, winning = line.split("|")
    card, numbers = scratch.split(":")

    game_id = int(card[5:])

    scratch_list = numbers.split(" ")
    winning_list = winning.split(" ")

    game_total = 0

    for num in scratch_list:
        if num.strip() == "":
            continue
        if num in winning_list:
            game_total += 1

    for index in range(game_id, game_id + game_total):
        if index < len(scratchcards):
            scratchcards[index] += scratchcards[game_id - 1]
# original set
total = 0
for count in scratchcards:
    total += count
print(total)
