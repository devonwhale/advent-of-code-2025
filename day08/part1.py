import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

junction_boxes = []
for line in input:
    split_line = line.split(',')
    junction_boxes.append({'x': int(split_line[0]), 'y': int(split_line[1]), 'z': int(split_line[2])})

distances = []
idx = 0
for box in junction_boxes:
    for next_box_idx in range(idx + 1, len(junction_boxes)):
        next_box = junction_boxes[next_box_idx]
        distances.append({'box_a': idx, 'box_b': next_box_idx, 'distance': ((box['x'] - next_box['x']) ** 2) + ((box['y'] - next_box['y']) ** 2) + ((box['z'] - next_box['z']) ** 2)})
    idx += 1

distances.sort(key=lambda box_pair: box_pair['distance'])

number_of_conections_to_make = 1000
circuits = {}
for idx in range(0, len(junction_boxes)):
    circuits[idx] = [idx]

for i in range(0, number_of_conections_to_make):
    connection = distances.pop(0)
    connection_box_a = connection['box_a']
    connection_box_b = connection['box_b']
    connection_made = False
    for existing_circuit in circuits:
        if connection_box_a in circuits[existing_circuit] and connection_box_b in circuits[existing_circuit]:
            connection_made = True
            break
        if connection_box_a in circuits[existing_circuit] or connection_box_b in circuits[existing_circuit]:
            boxes_to_update = [connection_box_a, connection_box_b]
            boxes_to_update.extend(circuits[connection_box_a])
            boxes_to_update.extend(circuits[connection_box_b])
            for box in set(boxes_to_update):
                for other_box in set(boxes_to_update):
                    if other_box not in circuits[box]:
                        circuits[box].append(other_box)
                        circuits[other_box].append(box)
            break

unique_circuits = []
for circuit in circuits:
    set_circuit = set(circuits[circuit])
    if set_circuit not in unique_circuits:
        unique_circuits.append(set_circuit)

unique_circuits.sort(reverse=True, key=lambda c: len(c))
print(len(unique_circuits[0]) * len(unique_circuits[1]) * len(unique_circuits[2]))