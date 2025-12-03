import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for bank in input:
    batteries = list(bank)
    allowed_count = 12
    selected_batteries = ['0'] * allowed_count
    locked_idx = 0
    battery_idx = 0
    for battery in batteries:
        # find all the places it could go in the final list
        potential_positions = []
        assessment_position = 0
        for sb in selected_batteries:
            if assessment_position < locked_idx:
                assessment_position += 1
                continue
            if battery > sb:
                potential_positions.append(assessment_position)
            assessment_position += 1
        
        # iterate through them
        for potential_position in potential_positions:
            required_batteries_for_complete_set = allowed_count - potential_position
            batteries_remaining = len(batteries) - battery_idx
            # does placing it here leave enough future batteries to have a complete set
              # if yes, place it here and move onto the next battery
              # if not, move onto the next possible space
            if batteries_remaining < required_batteries_for_complete_set:
                continue
            else:
                selected_batteries[potential_position] = battery
                for remaining_battery in range(potential_position + 1, allowed_count):
                    selected_batteries[remaining_battery] = '0'
                break
        battery_idx += 1
    
    bank_value = int(''.join(selected_batteries))
    output += bank_value

print(output)

