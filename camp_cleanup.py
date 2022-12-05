# In how many assignment pairs does one range fully contain the other?
import os, sys

def get_assignment_parts(assignment):
    comma_location = assignment.index(',')
    part_one = assignment[0:comma_location]
    part_two = assignment[comma_location + 1:len(assignment)]
    first_dash = part_one.index('-')
    second_dash = part_two.index('-')

    a = part_one[0:first_dash]
    b = part_one[first_dash + 1:len(part_one)]
    c = part_two[0:second_dash]
    d = part_two[second_dash + 1:len(part_two)]

    parts = (a, b, c, d)
    return parts

def fully_contained(assignment):
    parts = get_assignment_parts(assignment)
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    d = int(parts[3])
    
    if d - b >= 0 and c - a <= 0 or b - d >= 0 and a - c <=0:
        contained = True
    else:
        contained = False

    return contained

def any_overlap(assignment):
    parts = get_assignment_parts(assignment)
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    d = int(parts[3])

    if d >= a and c <= b or a <= d and c <= b:
        overlap = True
    else:
        overlap = False

    return overlap

def main():
    # read raw data into list
    raw_data_path = os.path.join(sys.path[0], 'day_4_input.txt')
    with open(raw_data_path) as raw_data:
        cleaning_assignments = raw_data.readlines()

    fully_contained_ct = 0
    any_overlap_ct = 0

    for assignment in cleaning_assignments:
        if fully_contained(assignment.strip()) == True:
            fully_contained_ct = fully_contained_ct + 1
        if any_overlap(assignment.strip()) == True:
            any_overlap_ct = any_overlap_ct + 1
    
    print('Assignment pairs with full overlap: ' + str(fully_contained_ct))
    print('Assignments with any overlap: ' + str(any_overlap_ct))
    return

main()