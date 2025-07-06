#!/usr/bin/env python3

import re

def parse_instructions(file):
    with open(file) as file:
        input = file.read().strip()
        instructions = re.split(r",\s",input)
    return instructions

def get_coords_for_move(start_coord, num_blocks, direction):
    coords=[]
    current_coord = start_coord
    if direction == "N":
        for n in range(num_blocks):
            step_coord = (current_coord[0],current_coord[1] + 1)
            coords.append(step_coord)
            current_coord = coords[-1]
    elif direction == "E":
        for n in range(num_blocks):
            step_coord = (current_coord[0] + 1,current_coord[1])
            coords.append(step_coord)
            current_coord = coords[-1]
    elif direction == "S":
        for n in range(num_blocks):
            step_coord = (current_coord[0],current_coord[1] - 1)
            coords.append(step_coord)
            current_coord = coords[-1]
    elif direction == "W":
        for n in range(num_blocks):
            step_coord = (current_coord[0] - 1,current_coord[1])
            coords.append(step_coord)
            current_coord = coords[-1]
    else:
        print("Error - direction not found")
        exit(1)
    return coords

instructions = parse_instructions("/Users/cc52/repositories/personal/aoc-10y/day1/2016/test_input.txt")
directions = ["N","E","S","W"]

# Set up direction trackers
current_direction = directions[0]
steps_north = 0
steps_east = 0
steps_south = 0
steps_west = 0

# Initiate coordinates history
current_coord = (0,0)
coord_hist = [current_coord]
return_coord = []

for instruction in instructions:
    # Parse the instruction
    rotation = re.search(r'\w', instruction).group()
    i = directions.index(current_direction)

    # First update current direction
    if current_direction == directions[0] and rotation == "L":
        current_direction = directions[3]
    elif current_direction == directions[3] and rotation == "R":
        current_direction = directions[0]
    elif instruction.startswith("L"):
        current_direction = directions[i-1]
    elif instruction.startswith("R"):
        current_direction = directions[i+1]
    else:
        print("Incorrect character found in instruction, only L and R accepted!")
        exit(1)
    
    # Then add the number of blocks to the correct direction tally
    current_blocks = int(re.search(r'\d+', instruction).group())
    new_coords = get_coords_for_move(current_coord, current_blocks, current_direction)

    for coord in new_coords:
        if coord in coord_hist:
            return_coord.append(coord)
    coord_hist.extend(new_coords)
    current_coord = new_coords[-1]

y_blocks = steps_north - steps_south
x_blocks = steps_east - steps_west
total_blocks = abs(x_blocks) + abs(y_blocks)

first_return_coords = return_coord[0]
first_return_blocks = abs(first_return_coords[0]) + abs(first_return_coords[1])

print(return_coord)
print(len(coord_hist))
print(len(instructions))
print(f"Steps North: {steps_north}, Steps East: {steps_east}, Steps South: {steps_south}, Steps West: {steps_west}")
print(f"Minimum number of blocks away: {total_blocks}")
print(f"First returned to {first_return_coords}, {first_return_blocks} blocks away from origin.")