#!/usr/bin/env python3

# Initiate floor counter & boolean for basement condition
floor=0
subterranean=False

# Read in input and loop through characters
with open("input.txt") as file:
    input=file.read().strip()

for index, instruction in enumerate(input):
    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1
    else:
        print("Unexpected character in input.")

    if floor < 0:
        basement_instruction = index + 1
        print(f"Basement reached at instruction number {basement_instruction}")
        break