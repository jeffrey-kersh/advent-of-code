import os, sys

# get file path of raw data
raw_data_path = os.path.join(sys.path[0], 'day_1_input.txt')

# read raw data into list
with open(raw_data_path) as f:
    lines = f.readlines()

# initialize variables
totalCalories = []
cal = 0

# loop through all lines
for line in lines:
    # if line is empty
    if not line.strip():
        # new elf - add total to list of totals & reset calories
        totalCalories.append(cal)
        cal = 0
    else:
        # add calories from that line to running total
        cal = cal + int(line.strip())

# get maximum value
maxCal = max(totalCalories)

# order list descending
totalCalories.sort(reverse=True)

# sum first three greatest values
topThreeCals = totalCalories[0] + totalCalories[1] + totalCalories[2]

# display answers
print('Highest Elf\'s Calorie Count: ' + str(maxCal))
print('Sum of Top Three Elf\'s Calorie Counts: ' + str(topThreeCals))