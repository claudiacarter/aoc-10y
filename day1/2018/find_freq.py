#!/usr/bin/env python3

def get_input(text_file):
    with open(text_file) as file:
        input = file.read().splitlines()
    return input
# Initiate frequency tracker
frequency = 0
freq_changes = get_input("input.txt")

for change in freq_changes:
    frequency += int(change)

print(f"The final frequency is {frequency}")


