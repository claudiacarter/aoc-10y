#!/usr/bin/env python3

# Read in input and add first character to end for circularity
with open("input.txt") as file:
    input = file.read().strip()

length = len(input)
print(f"The input is {length} digits long.")
list_input = list(input)

'''
Part One Answer
'''
# Fill a list with digits to sum
to_add = []

# Get digits matching conditions up to the penultimate
for i in range(len(list_input)-1):
    if list_input[i] == list_input[i+1]:
        to_add.append(list_input[i])
# Catch last case
if list_input[-1] == list_input[0]:
    to_add.append(list_input[-1])

# Sum digits and print answer to Part One
answer_1 = 0
for digit in to_add:
    answer_1 = answer_1 + int(digit)
print(f"Sum of all digits equal to subsequent digit: {answer_1}")

'''
Part Two Answer
'''
index_dist = int(length/2)

answer_2 = 0

# Treat the first and second halves of the input differently
first_half = list_input[:index_dist]
for i,digit in enumerate(first_half):
    if int(digit) == int(list_input[i+index_dist]):
        answer_2 += int(digit)
second_half = list_input[index_dist:]
for i,digit in enumerate(second_half):
    if int(digit) == int(list_input[i]):
        answer_2 += int(digit)

print(f"Sum of all digits equal to that {index_dist} indexes ahead: {answer_2}.")


