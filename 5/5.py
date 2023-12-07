with open("D:\\Documents\\GitHub\\advent-of-code-2023\\5\\input5.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

seeds = lines[0]

lines = [line.split(" ") for line in lines]

seed_to_soil = lines[3:38]
soil_to_fertlizer = lines[40:73]
fertilizer_to_water = lines[75:103]
water_to_light = lines[105:120]
light_to_temperature = lines[122:154]
temperature_to_humidity = lines[156:188]
humidity_to_location = lines[190:206]


def in_range(seed, mins, ranges):
    return int(seed) >= int(mins) and (int(seed) < (int(mins) + int(ranges)))


def get_dest_list(source_list, mapping):
    ls = []
    for seed in source_list:
        for transfer in mapping:
            starting_dest = transfer[0]
            starting_source = transfer[1]
            index_range = transfer[2]
            if in_range(seed, starting_source, index_range):
                ls.append(int(starting_dest) + (int(seed) - int(starting_source)))
                break
    return ls


# get lowest location number that corresponds to any initial seed numbers
seeds = seeds.split(" ")

# remove words
seeds.pop(0)


# go through all conversions using generic function
soils = get_dest_list(seeds, seed_to_soil)
fertilizers = get_dest_list(soils, soil_to_fertlizer)
waters = get_dest_list(fertilizers, fertilizer_to_water)
lights = get_dest_list(waters, water_to_light)
temperatures = get_dest_list(lights, light_to_temperature)
humidities = get_dest_list(temperatures, temperature_to_humidity)
locations = get_dest_list(humidities, humidity_to_location)


# everything is still in order so finding the index of the last=index of the first
min_location = min(locations)

# print seed with min location
print(min_location)
