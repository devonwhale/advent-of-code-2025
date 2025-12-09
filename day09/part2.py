import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

from shapely.geometry.polygon import Polygon

coords = [{'x': int(line.split(',')[0]), 'y': int(line.split(',')[1])} for line in input]
shape = Polygon([[int(line.split(',')[0]), int(line.split(',')[1])] for line in input])

polygon_lines = []
max_x, max_y = 0, 0

for i in range(-1, len(coords) - 1):
    line_start = coords[i]
    line_end = coords[i + 1]
    if line_start['x'] > max_x:
        max_x = line_start['x']
    if line_start['y'] > max_y:
        max_y = line_start['y']
    polygon_lines.append((line_start['x'], line_start['y'], line_end['x'], line_end['y']))

idx = 1
max_area = 0
areas = []
for coord in coords:
    for other_coord_idx in range(idx, len(coords)):
        other_coord = coords[other_coord_idx]

        lower_x = min(coord['x'], other_coord['x'])
        upper_x = max(coord['x'], other_coord['x'])
        x_distance = upper_x - lower_x + 1

        lower_y = min(coord['y'], other_coord['y'])
        upper_y = max(coord['y'], other_coord['y'])
        y_distance = upper_y - lower_y + 1

        area = x_distance * y_distance
        areas.append({'coord_a': coord, 'coord_b': other_coord, 'area': area})
        if area > max_area:
            inner_shape = Polygon([(coord['x'], coord['y']), (coord['x'], other_coord['y']), (other_coord['x'], other_coord['y']), (other_coord['x'], coord['y'])])

            if shape.contains(inner_shape):
                max_area = area
    idx += 1

print(max_area)