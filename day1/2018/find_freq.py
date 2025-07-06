#!/usr/bin/env python3

def get_input(text_file):
    with open(text_file) as file:
        input = file.read().splitlines()
    return input
# Initiate frequency trackers
final_frequency = 0
freq_history = [final_frequency]

# Extract and apply frequency changes from input
freq_changes = get_input("input.txt")
for change in freq_changes:
    final_frequency += int(change)
    freq_history.append(final_frequency)

# Answer to Part One
print(f"The final frequency is {final_frequency}")


# Initialise a bool for finding the first revisited frequency
revisit_event = False

# Check if there are any repeats in the first loop of changes
for i,freq in enumerate(freq_history):
    if freq in freq_history[:i]:
        print(f"This frequency is revisited: {freq}")
        revisit_event = True
        break

if not revisit_event:
    print("No frequencies repeated in single loop.")
    print("Looping until a repeat is found.")
else:
    exit(0)

loops = 0
current_frequency = final_frequency
non_redundant_freqs = set(freq_history)

# Each set of frequencies from a new loop of changes is shifted by the final frequency
while revisit_event == False:
    loops += 1
    for change in freq_changes:
        current_frequency += int(change)
        if current_frequency in non_redundant_freqs:
            print(f"This frequency is revisited: {current_frequency}")
            revisit_event = True
            break
        else:
            non_redundant_freqs.add(current_frequency)
print(f"Found after {loops} loops.")
