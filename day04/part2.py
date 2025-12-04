import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

grid = []

y = 0
for line in input:
    grid.append([])
    for char in list(line):
        grid[y].append(char)
    y += 1

output = 0
another_cycle = True

while another_cycle:
    y = 0
    locations_to_remove = []
    for row in grid:
        x = 0
        for location in row:
            if location == '.':
                x += 1
                continue

            positions_to_check = []
            if y != 0:
                positions_to_check.append({'x': 0, 'y': -1})
                if x != 0:
                    positions_to_check.append({'x': -1, 'y': -1})
                if x != len(row) - 1:
                    positions_to_check.append({'x': 1, 'y': -1})
            if y != len(grid) - 1:
                positions_to_check.append({'x': 0, 'y': 1})
                if x != 0:
                    positions_to_check.append({'x': -1, 'y': 1})
                if x != len(row) - 1:
                    positions_to_check.append({'x': 1, 'y': 1})
            if x != 0:
                    positions_to_check.append({'x': -1, 'y': 0})
            if x != len(grid) - 1:
                    positions_to_check.append({'x': 1, 'y': 0})

            adjacent_count = 0
            for position in positions_to_check:
                if grid[y + position['y']][x + position['x']] == '@':
                    adjacent_count += 1

            if adjacent_count < 4:
                output += 1
                locations_to_remove.append({'x': x, 'y': y})
            x += 1
        y += 1

    for location in locations_to_remove:
        grid[location['y']][location['x']] = '.'

    if len(locations_to_remove) == 0:
        another_cycle = False

print(output)