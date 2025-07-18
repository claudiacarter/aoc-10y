#!/usr/bin/env python3

from collections import Counter

def get_input(text_file):
    with open(text_file) as file:
        return list(map(int, file.read().splitlines()))

def compare_to_prev (depth, prev):
    if depth < prev:
        change = -1
    elif depth == prev:
        change = 0
    else:
        change = 1
    return change

def add_trios(full_measurements):
    trios = []
    end = len(full_measurements)
    for i in range(end-2):
        total = full_measurements[i] + full_measurements[i+1] + full_measurements[i+2]
        trios.append(total)
    return trios


#PART1
depths = get_input("/Users/cc52/repositories/personal/aoc-10y/day1/2021/input.txt")
changes =[]

for i, depth in enumerate(depths):
    if i == 0:
        pass
    else:
        change = compare_to_prev(depths[i], depths[i - 1])
        changes.append(change)

counts = Counter(changes)

print(counts)

#PART2
trios = add_trios(depths)

changes =[]

for i, trio in enumerate(trios):
    if i == 0:
        pass
    else:
        change = compare_to_prev(trios[i], trios[i - 1])
        changes.append(change)

counts = Counter(changes)

print(counts)
