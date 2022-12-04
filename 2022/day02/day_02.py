data = open('input.txt').read().split("\n")
# A, X - Rock       (1p)
# B, Y - Paper      (2p)
# C, Z - Scissors   (3p)
# Win  (6p)
# Even (3p)
# Loss (0p)
response_score = {'X': 1, 'Y': 2, 'Z': 3}
game_score = {('A', 'Y'): 6, ('A', 'Z'): 0, ('A', 'X'): 3,
              ('B', 'Z'): 6, ('B', 'X'): 0, ('B', 'Y'): 3,
              ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}

total_score = 0
for deal in data:
    opponent = deal[0]
    response = deal[2]
    total_score += response_score[response]
    total_score += game_score[(opponent, response)]
# Part 1:  11475
print("Part 1: ", total_score)

# X - I need to lose
# Y - I need to draw
# Z - I need to win
response_regarding = {('A', 'X'): 'Z', ('A', 'Y'): 'X', ('A', 'Z'): 'Y',
                      ('B', 'X'): 'X', ('B', 'Y'): 'Y', ('B', 'Z'): 'Z',
                      ('C', 'X'): 'Y', ('C', 'Y'): 'Z', ('C', 'Z'): 'X'}
total_score = 0
for deal in data:
    opponent = deal[0]
    what_to_do = deal[2]
    response = response_regarding[(opponent, what_to_do)]
    total_score += response_score[response]
    total_score += game_score[(opponent, response)]
# Part 2:  16862
print("Part 2: ", total_score)

