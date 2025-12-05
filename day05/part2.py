import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

fresh_values = []
output = 0
for line in input:
    if line == '':
        break
    else:
        split_line = line.split('-')
        fresh_values.append({'start': int(split_line[0]), 'end': int(split_line[1]) + 1})

fresh_values.sort(key=lambda value_range: value_range['start'])

lengths = []

idx = 0
for fv in fresh_values:
    start = fv['start']
    end = fv['end']
    idx_to_remove = []
    for i in range(idx + 1, len(fresh_values)):
        if i >= len(fresh_values):
            break
        other_start = fresh_values[i]['start']
        other_end = fresh_values[i]['end']

        other_start_within_range = start <= other_start and other_start <= end
        other_end_beyond_range = start <= other_end and end <= other_end

        if other_start_within_range and other_end_beyond_range:
            idx_to_remove.append(i)
            end = other_end
        elif start <= other_start and other_end <= end:
            idx_to_remove.append(i)
        else: 
            break
    
    if len(idx_to_remove) > 0:
        idx_to_remove.sort(reverse=True)
        for i in idx_to_remove:
            del fresh_values[i]
    
    output += end - start
    idx += 1
    

print(output)