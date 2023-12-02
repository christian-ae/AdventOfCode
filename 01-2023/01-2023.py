import numpy as np

input = np.loadtxt('input2.txt', dtype=str)

# Part 2
spelled_ints = ["one","two","three","four","five","six","seven","eight","nine"]
convert_int = ["1","2","3","4","5","6","7","8","9"]

sum = 0
for str in input:
    char_list = []
    substring = ""
    for i, char in enumerate(str):
        if char.isnumeric():
            char_list.append(char)
        else:
            substring += char
        for i, spelled_int in enumerate(spelled_ints):
            if spelled_int in substring:
                char_list.append(convert_int[i])
                substring = substring[-1]
    sum += int(char_list[0] + char_list[-1])
    char_list.clear()

print(sum)
