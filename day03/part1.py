import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for bank in input:
    batteries = list(bank)
    best_batteries = ['0'] * 2
    b_idx = 0
    for battery in batteries:
      bb_idx = 0
      for bb in best_batteries:
        if battery > bb:
          if b_idx == len(bank) - 1 and bb_idx < len(best_batteries) - 1:
             bb_idx += 1
             continue
          best_batteries[bb_idx] = battery
          for i in range(bb_idx + 1, len(best_batteries)):
             best_batteries[i] = '0'
          break
        bb_idx += 1
      b_idx += 1

    output += int(best_batteries[0] + best_batteries[1])

print(output)