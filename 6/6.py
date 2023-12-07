with open("D:\\Documents\\GitHub\\advent-of-code-2023\\6\\input6.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

times = lines[0].split()
distances = lines[1].split()

times.pop(0)
distances.pop(0)

times = [int(x) for x in times]
distances = [int(x) for x in distances]


error_margin = 1
for i in range(len(times)):
    wins = 0
    for time_held in range(times[i]):
        time_running = times[i] - time_held
        # time held is the same as speed
        total_distance = time_running * time_held
        print(
            f"speed: {time_held},\n time_running: {time_running} \n{total_distance}>{distances[i]}"
        )
        if total_distance > distances[i]:
            wins += 1
    error_margin *= wins

print(error_margin)
