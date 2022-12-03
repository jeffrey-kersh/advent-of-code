import os, sys

# find winner
def get_round_outcome(my_move, elf_move):
    if my_move == 'X':
        if elf_move == 'B':
            win_status = 'L'
        elif elf_move == 'C':
            win_status = 'W'
        else:
            win_status = 'D'
    elif my_move == 'Y':
        if elf_move == 'A':
            win_status = 'W'
        elif elf_move == 'C':
            win_status = 'L'
        else:
            win_status = 'D'
    elif my_move == 'Z':
        if elf_move == 'A':
            win_status = 'L'
        elif elf_move == 'B':
            win_status = 'W'
        else:
            win_status = 'D'
    return win_status

# calculate round score
def get_round_score(moves):
    round_score = 0
    my_move = moves[2]
    elf_move = moves[0]
    # print('My Move: ' + my_move + ' | Elf Move: ' + elf_move)

    # get points for selection
    if my_move == 'X':
        round_score = round_score + 1
    elif my_move == 'Y':
        round_score = round_score + 2
    elif my_move == 'Z':
        round_score = round_score + 3

    # get points for win/loss/draw
    outcome = get_round_outcome(my_move, elf_move)
    if outcome == 'W':
        round_score = round_score + 6
    elif outcome == 'L':
        round_score = round_score + 0
    elif outcome == 'D':
        round_score = round_score + 3

    return round_score

# get file path of raw data
raw_data_path = os.path.join(sys.path[0], 'day_2_input.txt')

# read raw data into list
with open(raw_data_path) as raw_data:
    strategy_guide = raw_data.readlines()

# remove new lines
strategy_guide = [item.strip() for item in strategy_guide]
total_score = 0

# loop through each round
for round in strategy_guide:
    # add round score to total
    total_score = total_score + get_round_score(round)

print('Total Score: ' + str(total_score))