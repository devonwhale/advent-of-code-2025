import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

fresh_values = []
ingredients = []
output = 0
parsing_ingredients = False
for line in input:
    if line == '':
        parsing_ingredients = True
    elif parsing_ingredients:
        ingredients.append(int(line))
    else:
        split_line = line.split('-')
        fresh_values.append(range(int(split_line[0]), int(split_line[1]) + 1))

for i in ingredients:
    for fv in fresh_values:
        if i in fv:
            output += 1
            break

print(output)