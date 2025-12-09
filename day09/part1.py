import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

coords = [{'x': int(line.split(',')[0]), 'y': int(line.split(',')[1])} for line in input]

max_area = 0
idx = 1
for coord in coords:
    for other_coord_idx in range(idx, len(coords)):
        other_coord = coords[other_coord_idx]
        x_distance = 1
        if coord['x'] > other_coord['x']:
            x_distance = coord['x'] - other_coord['x'] + 1
        elif coord['x'] < other_coord['x']:
            x_distance  = other_coord['x'] - coord['x'] + 1
        
        y_distance = 1
        if coord['y'] > other_coord['y']:
            y_distance = coord['y'] - other_coord['y'] + 1
        elif coord['y'] < other_coord['y']:
            y_distance  = other_coord['y'] - coord['y'] + 1
        
        area = x_distance * y_distance
        if area > max_area:
            max_area = area
    idx += 1

print(max_area)