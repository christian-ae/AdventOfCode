#12 red
#13 green
#14 blue

import numpy as np


#Part one
input = open("input.txt", "r")
input = input.read().split("\n")

cube_limits = np.array([12, 13, 14])

sum = 0
power = 0
for idx, line in enumerate(input[:100]):

    max_cube_count = [0,0,0]
    line = line.replace("Game " + str(idx+1) + ": ", "").replace(";", "").replace(",", "")
    line = line.split(" ")

    #NOTE: This can be turned into a for-loop
    max_cube_count[0] = max([int(line[index-1]) for (index, item) in enumerate(line) if item == "red"])
    max_cube_count[1] = max([int(line[index-1]) for (index, item) in enumerate(line) if item == "green"])
    max_cube_count[2] = max([int(line[index-1]) for (index, item) in enumerate(line) if item == "blue"])

    values = cube_limits - max_cube_count
    if np.any(values < 0):
        print("Game " + str(idx+1) + " is invalid")
        #print(line)
    else:
        sum += idx + 1
    power += np.prod(np.asarray(max_cube_count))

print(sum)
print(power)
#Part two
