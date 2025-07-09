#!/usr/bin/env python3

import math

def get_input(text_file):
    with open(text_file) as file:
        input = file.read().splitlines()
    return input

def find_sum_partners(number, total):
    required_partner = total - number
    return required_partner

entry_list = [int(entry) for entry in sorted(get_input("input.txt"), key=int)]


# Part 1
print("Part 1 - Find the two numbers that add to 2020")
for entry in entry_list:
    pair = find_sum_partners(entry,2020)
    if pair in entry_list:
        print(f"Entry {entry} and {pair} add up to 2020")
        key_entry1 = entry
        key_entry2 = pair

answer1 = key_entry1 * key_entry2

print(f"{key_entry1} * {key_entry2} = {answer1}")

# Part 2
print("Part 2 - Find the three numbers that add to 2020")

trio = []
            
for trio1 in entry_list:
    remainder = find_sum_partners(trio1,2020)
    for potential_trio2 in entry_list:
        trio3 = find_sum_partners(potential_trio2, remainder)
        if trio3 in entry_list:
            trio.append(trio1)
            trio.append(potential_trio2)
            trio.append(trio3)
            break

answer2 = math.prod(set(trio))
print(f"These add up to 2020: {set(trio)}")
print(f"Answer to part 2: {answer2}")