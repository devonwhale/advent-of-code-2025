import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

dial = 50
count = 0

for instruction in input:
    movement_distance = int(instruction[1:])
    if instruction[0] == 'R':
        for tick in range(0, movement_distance):
            dial += 1
            if dial == 100:
                dial = 0
                count += 1
    else:
        for tick in range(0, movement_distance):
            dial -= 1
            if dial == 0:
                count += 1
            if dial == -1:
                dial = 99

print(count)