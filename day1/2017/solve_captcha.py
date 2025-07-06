#!/usr/bin/env python3

# Read in input and add first character to end for circularity
with open("input.txt") as file:
    input = file.read().strip()
list_input = list(input)
list_input.append(input[0])

# Fill a list with digits to sum
to_add = []

for i in range(len(list_input)-1):
    if list_input[i] == list_input[i+1]:
        to_add.append(list_input[i])

# Sum digits and print answer
working_total = 0
for digit in to_add:
    working_total = working_total + int(digit)
print(working_total)