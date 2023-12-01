import numpy as np
from collections import defaultdict


def change_order(current_order):
    new_order = {}
    for k, v in current_order.items():
        k -= 1
        if k == 0:
            new_order[4] = v
        else:
            new_order[k] = v
    return new_order


def read_data(file_name='input.txt'):
    return open(file_name).read().split("\n")


#       ^ x (North is positive)
#       |
#       +----> y (East is positive)
#
#   Directions are N: [1, 0], E: [0, 1], S: [-1, 0], W: [0, -1]
#
#          \ ^ /
#          < # >     # is elf, checks around itself. Diagonals are NE, SE, SW and NW
#          / v \       NE: [1, 1], SE: [-1, 1], SW: [-1, -1], NW: [1, -1]
#
directions = {'N': np.array([1, 0]),
              'NE': np.array([1, 1]),
              'SE': np.array([-1, 1]),
              'SW': np.array([-1, -1]),
              'NW': np.array([1, -1]),
              'E': np.array([0, 1]),
              'S': np.array([-1, 0]),
              'W': np.array([0, -1])}
# N, NE, E, SE, S, SW, W, NW
adjacent = np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]])

data = read_data('input.txt')
data.reverse()
elf_at = defaultdict()
elf_pos = np.array([])
x = 0
for line in data:
    y = 0
    for c in line:
        if c == '#':
            elf_at[(x, y)] = True
            elf_pos = np.append(elf_pos, np.array([x, y]))
        y += 1
    x += 1
elf_pos = elf_pos.reshape(len(elf_pos)//2, 2)
order_of_instructions = {1: ['N', 'NE', 'NW'], 2: ['S', 'SE', 'SW'], 3: ['W', 'NW', 'SW'], 4: ['E', 'NE', 'SE']}

for round_number in range(1, 10 + 1):
    # First half
    # During the first half of each round, each Elf considers the eight positions adjacent to themself.
    # If no other Elves are in one of those eight positions, the Elf does not do anything during this round.
    # Otherwise, the Elf looks in each of four directions in the following order
    #    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    #    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    #    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    #    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
    # and proposes moving one step in the first valid direction:
    elfs_that_can_move = []
    for elf in elf_pos:
        adjacent_positions = elf + adjacent
        elf_should_move = False
        for p in adjacent_positions:
            if elf_at.__contains__((p[0], p[1])):  # An elf is close, should move
                elf_should_move = True
        if elf_should_move:
            elfs_that_can_move.append(elf)
    elf_move_proposal = defaultdict()
    for elf in elfs_that_can_move:  # The elf
        for i in range(1, 4 + 1):  # looks in each of four directions
            directions_to_check = order_of_instructions[i]  # in the following order
            can_move_in_this_direction = True
            for direction in directions_to_check:
                check_this_positions = elf + directions[direction]
                if elf_at.__contains__((check_this_positions[0], check_this_positions[1])):
                    # Can't move in directions_to_check[0]
                    can_move_in_this_direction = False
                    break
            if can_move_in_this_direction:  # proposes moving one step in the first valid direction:
                move_direction = directions_to_check[0]
                move_proposal = elf + directions[move_direction]
                elf_move_proposal[(elf[0], elf[1])] = move_proposal
    # Second half
    # After each Elf has had a chance to propose a move, the second half of the round can begin.
    # Simultaneously,
    #   each Elf moves to their proposed destination tile
    #   if they were the ONLY Elf to propose moving to that position.
    #   If two or more Elves propose moving to the same position, NONE of those Elves move.
    index = 0
    values = [x for x in elf_move_proposal.values()]
    for elf, move in elf_move_proposal.items():
        if np.count_nonzero(move == values)//2 == 1:  #if move is unique
            current_pos = np.array(elf)
            index = np.argwhere((elf_pos == current_pos).all(1))[0][0]
            # execute
        #else no elf with that move may execute
        index += 1
    # Finally
    break




# Finally, at the end of the round,
# the first direction the Elves considered is moved to the end of the list of directions.
# For example, during the second round,
#   the Elves would try proposing a move to the south first,
#   then west, then east, then north.
# On the third round,
#   the Elves would first consider west, then east, then north, then south.

# Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds.
# How many empty ground tiles does that rectangle contain?