import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = [list(line) for line in input]

current_beam_positions = [rows[0].index('S')]

output = 0
for depth in range(1, len(rows)):
    new_positions = []
    for beam in current_beam_positions:
        if rows[depth][beam] == '.':
            new_positions.append(beam)
        elif rows[depth][beam] == '^':
            if beam > 0:
                new_positions.append(beam - 1)
            if beam < len(rows[depth]):
                new_positions.append(beam + 1)
            output += 1
    current_beam_positions = list(set(new_positions))

print(output)