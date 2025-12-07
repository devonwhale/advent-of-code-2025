import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = [list(line) for line in input]

cache = {}

def assess_next_level(target_depth, index):
    if target_depth == len(rows) - 1:
        if (target_depth, index) not in cache:
            cache[(target_depth, index)] = 0
        cache[(target_depth, index)] += 1
        return 1

    if (target_depth, index) in cache:
        return cache[(target_depth, index)]
    
    next_value = rows[target_depth][index]
    next_locations = []    
    if next_value == '.':
        next_locations.append((target_depth + 1, index))
    elif next_value == '^':
        if index > 0:
            next_locations.append((target_depth, index - 1))
        if index < len(rows[target_depth]):
            next_locations.append((target_depth, index + 1))

    beam_count = 0

    for location in next_locations:
        beam_count += assess_next_level(location[0], location[1])
    
    if (target_depth, index) not in cache:
        cache[(target_depth, index)] = 0
    cache[(target_depth, index)] += beam_count

    return beam_count

output = assess_next_level(1, rows[0].index('S'))

print(output)