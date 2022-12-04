import os, sys

def get_badge(elf_one, elf_two, elf_three):
    common_items = []
    for item in elf_one:
        for other_item in elf_two:
            if item == other_item:
                common_items.append(item)
    for item in elf_three:
        for other_item in common_items:
            if item == other_item:
                badge = item
    return badge

# list priorities
priority_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

# read raw data into list
raw_data_path = os.path.join(sys.path[0], 'day_3_input.txt')
with open(raw_data_path) as raw_data:
    rucksack_data = raw_data.readlines()

priorities_sum = 0

for rucksack in rucksack_data:
    rucksack = rucksack.strip()
    mid = int(len(rucksack)/2)
    end = len(rucksack)
    front_compartment = rucksack[0:mid]
    back_compartment = rucksack[mid:end]
    for f_item in front_compartment:
        for b_item in back_compartment:
            if f_item == b_item:
                priority = priority_dict[f_item]
                priorities_sum = priorities_sum + priority
                break
        if f_item == b_item:
            break

print('Part 1 Sum: ' + str(priorities_sum))

# get group data
group_priorities_sum = 0
i = 0
group_first_indeces = []

while i < len(rucksack_data):
    group_first_indeces.append(i)
    i = i + 3

x = 1
for group in group_first_indeces:
    elf_one = rucksack_data[group].strip()
    elf_two = rucksack_data[group + 1].strip()
    elf_three = rucksack_data[group + 2].strip()
    badge = get_badge(elf_one, elf_two, elf_three)
    priority = priority_dict[badge]
    group_priorities_sum = group_priorities_sum + priority

print('Part 2 Sum: ' + str(group_priorities_sum))