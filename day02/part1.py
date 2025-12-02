import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

parsed_input = input[0].split(',')
output = 0

for product_ids in parsed_input:
    split_id_range = product_ids.split('-')
    for id in range(int(split_id_range[0]), int(split_id_range[1]) + 1):
        string_id = str(id)
        half_length = int(len(string_id)/2)
        if string_id[:half_length] == string_id[half_length:]: 
          output += id

print(output)