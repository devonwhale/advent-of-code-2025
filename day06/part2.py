import os, math
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = []

idx = 0
split_indexes = []
for i in range(0, len(input[0])):
    empty_count = 0
    for line in input:
        if line[i] == ' ':
            empty_count += 1
    if empty_count == len(input):
        split_indexes.append(i)

for line in input:
    split_line = []
    start_point = 0
    for split_point in split_indexes:
        split_line.append(line[start_point:split_point])
        start_point = split_point + 1
    split_line.append(line[start_point:])
    split_line.reverse()
    rows.append(split_line)
    idx += 1

number_of_calculations = len(rows[0])
number_of_inputs = len(rows) - 1
output = 0

for i in range(0, number_of_calculations):
    calculation = rows[number_of_inputs][i]
    values = []

    for j in range(0, number_of_inputs):
        values.append(rows[j][i])
    idx_to_search = len(max(values, key=len))

    parsed_values = []
    for j in range(idx_to_search, 0, -1):
        parsed_value = ''
        for v in values:
            if len(v) >= j:
                parsed_value += v[j - 1]
        parsed_values.append(int(parsed_value))
    
    if '*' in calculation:
        output += math.prod(parsed_values)
    elif '+' in calculation:
        output += sum(parsed_values)

print(output)