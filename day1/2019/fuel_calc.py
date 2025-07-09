#!/usr/bin/env python3
import math
from typing import List
'''
Every line is the mass of a module
To each line you want to divide by 3, round down and minus 2
'''

def get_input(text_file):
    with open(text_file) as file:
        input = file.read().splitlines()
    return input

def convert_mass_to_fuel(mass):
    tmp = int(mass) // 3
    fuel = tmp - 2
    return fuel


module_masses = get_input("input.txt")
module_fuel = [convert_mass_to_fuel(mass) for mass in module_masses]

answer_1 = sum(module_fuel)
print(f"Total fuel required for modules: {answer_1}")

total_fuel = 0
for mass in module_masses:
    fuel = convert_mass_to_fuel(mass)
    total_fuel += fuel
    while convert_mass_to_fuel(fuel) > 0:
        total_fuel += convert_mass_to_fuel(fuel)
        fuel = convert_mass_to_fuel(fuel)

# Answer 2 - includes fuel for fuel mass
print(f"Total fuel required for launch: {total_fuel}")

    
    


# #Initiate a list for fuel for fuel
# fuel_fuel_calcs = []

# # Start a conditional for fuel being negligible
# neg_fuel = False
# unfuelled_mass = module_fuel_calcs

# while not neg_fuel:
#     unfuelled_mass = convert_mass_to_fuel(unfuelled_mass)
#     if unfuelled_mass < 0:
#         neg_fuel == True
#         break
#     else:
#         fuel_fuel_calcs.append(unfuelled_mass)
    
# print(unfuelled_mass)






