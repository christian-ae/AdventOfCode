import numpy as np

input = np.loadtxt('input.txt', dtype=str)

sum = 0
for str in input:
    char_list = []
    for char in str:
        if char.isnumeric():
            char_list.append(char)
    sum += int(char_list[0]+char_list[-1])
    char_list.clear()
print(sum)