import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

dial = 50
count = 0

for instruction in input:
    if instruction[0] == 'R':
        dial += int(instruction[1:])
    else:
        dial -= int(instruction[1:])
    if dial % 100 == 0 or dial == 0:
        count += 1

print(count)