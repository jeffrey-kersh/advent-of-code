import os, sys

# pick my move
def get_my_move(desired_outcome, elf_move):
    # loss 
    if desired_outcome == 'X':
        if elf_move == 'A':
            my_move = 'Z'
        elif elf_move == 'B':
            my_move = 'X'
        elif elf_move == 'C':
            my_move = 'Y'
    # draw 
    elif desired_outcome == 'Y':
        if elf_move == 'A':
            my_move = 'X'
        elif elf_move == 'B':
            my_move = 'Y'
        elif elf_move == 'C':
            my_move = 'Z'
    # win
    elif desired_outcome == 'Z':
        if elf_move == 'A':
            my_move = 'Y'
        elif elf_move == 'B':
            my_move = 'Z'
        elif elf_move == 'C':
            my_move = 'X'
    return my_move

# calculate round score
def get_round_score(moves):
    round_score = 0
    elf_move = moves[0]
    desired_outcome = moves[2]

    # find my move
    my_move = get_my_move(desired_outcome, elf_move)

    # get points for selection
    if my_move == 'X':
        round_score = round_score + 1
    elif my_move == 'Y':
        round_score = round_score + 2
    elif my_move == 'Z':
        round_score = round_score + 3

    # get points for win/loss/draw
    if desired_outcome == 'Z':
        round_score = round_score + 6
    elif desired_outcome == 'X':
        round_score = round_score + 0
    elif desired_outcome == 'Y':
        round_score = round_score + 3

    return round_score

# read raw data into list
raw_data_path = os.path.join(sys.path[0], 'day_2_input.txt')
with open(raw_data_path) as raw_data:
    strategy_guide = raw_data.readlines()

# remove new lines
strategy_guide = [item.strip() for item in strategy_guide]
total_score = 0

# calculate total score
for round in strategy_guide:
    total_score = total_score + get_round_score(round)

print('Total Score: ' + str(total_score))