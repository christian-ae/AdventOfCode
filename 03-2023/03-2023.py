import numpy as np


#Part one
input = open("input.txt", "r")
input = input.read().split("\n")

data_matrix = []
for line in input:
    data_matrix.append(line.split(".")) 

print(data_matrix[1][2])

print(len(data_matrix[1]))
print(len(data_matrix[2]))

#Convert it into a square matrix first!!!!!


proximity_values = []
for i in range(0, len(data_matrix)):
    for j in range(0,len(data_matrix[1])):
        if data_matrix[i][j] != '' and data_matrix[i][j].isnumeric() == False:
            proximity_values.append(data_matrix[i-1][j])
            proximity_values.append(data_matrix[i+1][j])
            proximity_values.append(data_matrix[i][j-1])
            proximity_values.append(data_matrix[i][j+1])
            proximity_values.append(data_matrix[i-1][j+1])
            proximity_values.append(data_matrix[i+1][j-1])
            proximity_values.append(data_matrix[i-1][j-1])
            proximity_values.append(data_matrix[i+1][j+1])

print(proximity_values)