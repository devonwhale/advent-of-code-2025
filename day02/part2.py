import os, math
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

parsed_input = input[0].split(',')
output = 0

for product_ids in parsed_input:
    split_id_range = product_ids.split('-')
    for id in range(int(split_id_range[0]), int(split_id_range[1]) + 1):
        string_id = str(id)
        if len(string_id) == 1:
            continue
        length = len(string_id)
        factors = []
        for l in range(1, length + 1):
           if length % l == 0:
              factors.append(l)
        paired_factors = []
        for pair in range(0, math.ceil(len(factors)/2)):
            if len(factors) == 1:
                paired_factors.append((factors[0], factors[0]))
            else:
                paired_factors.append((factors[0], factors[-1]))
                if factors[0] != 1 and factors[1] != 1:
                    paired_factors.append((factors[-1], factors[0]))
                factors.pop(-1)
                factors.pop(0)

        for factor in paired_factors:
            split_id = []
            idx = 0
            for i in range(0, factor[1]):
                if idx == 0:
                    new_value = string_id[:factor[0]]
                else:
                    new_value = string_id[factor[0]*idx:factor[0]*idx+factor[0]]
                split_id.append(new_value)
                idx += 1

            if all(v == split_id[0] for v in split_id):
                output += id
                break

print(output)