class Machine:
    def __init__(self, target_lights, buttons, joltage):
        self.target_lights = target_lights
        self.buttons = buttons
        self.joltage = joltage

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

machines = []
for line in input:
    split_line = line.split(' ')
    lights, buttons, joltage = '', [], []
    for chunk in split_line:
        if '[' in chunk:
            lights = [True if b == '#' else False for b in chunk[1:-1]]
        elif '(' in chunk:
            buttons.append([int(b) for b in chunk[1:-1].split(',')])
        elif '{' in chunk:
            joltage = [int(b) for b in chunk[1:-1].split(',')]
    machines.append(Machine(lights, buttons, joltage))

def simulate_press(state, buttons):
    for button in buttons:
        current_state = state[button]
        state[button] = not current_state
    return state

output = 0
for machine in machines:
    attempt_list = [[i] for i in range(0, len(machine.buttons))]
    press_count = 1
    found_route = False
    while not found_route:
        for attempt in attempt_list:
            lights = [False] * len(machine.target_lights)
            for press in attempt:
                lights = simulate_press(lights, machine.buttons[press])
                if lights == machine.target_lights:
                    found_route = True
                    break
            if found_route:
                break 
        if not found_route:
            press_count += 1
            next_attempts = []
            for a in attempt_list:
                for b in range(0, len(machine.buttons)):
                    new_list = a.copy()
                    new_list.append(b)
                    next_attempts.append(new_list)
            attempt_list = next_attempts

    output += press_count

print(output)