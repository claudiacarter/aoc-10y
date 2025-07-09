#!/usr/bin/env python3

def get_input(text_file):
    with open(text_file) as file:
        input = file.read().splitlines()
    return input

entry_list = [int(entry) for entry in sorted(get_input("input.txt"), key=int)]



for entry in entry_list:
    required_pair = 2020 - entry
    if required_pair in entry_list:
        print(f"Entry {entry} and {required_pair} add up to 2020")
        break
answer1 = entry * required_pair

print(f"{entry} * {required_pair} = {answer1}")