#!/usr/bin/env python3
import math

'''
Every line is the mass of a module
To each line you want to divide by 3, round down and minus 2
'''

def get_input(text_file):
    with open(text_file) as file:
        input = file.read().splitlines()
    return input

module_masses = get_input("input.txt")
fuel_calcs = []

for mass in module_masses:
    tmp = int(mass) // 3
    fuel = tmp - 2
    fuel_calcs.append(fuel)

answer_1 = sum(fuel_calcs)
print(f"Total fuel required: {answer_1}")
