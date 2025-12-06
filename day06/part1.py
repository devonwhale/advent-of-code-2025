import os, math
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = []

final_line = len(input) - 1
idx = 0
for line in input:
    split_line = line.split(' ')
    while '' in split_line:
        split_line.remove('')
    if idx != final_line:
        split_line = [int(x) for x in split_line]
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
    if calculation == '*':
        output += math.prod(values)
    elif calculation == '+':
        output += sum(values)


print(output)