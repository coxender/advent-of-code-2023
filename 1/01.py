import re

with open("input1.txt","rt") as f:
    input_list = f.readlines()

total = 0

for line in input_list:
    num_list= re.findall(r'\d', line)
    if len(num_list)==1:
        total += int(num_list[0])*10+int(num_list[0])
    else:
        total += int(num_list[0])*10+int(num_list[-1])

print(total)
