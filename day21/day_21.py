import sys
sys.setrecursionlimit(40000)
#  Player 1 starting position: 2
#  Player 2 starting position: 8
visited_states = {}


class Dice:
    def __init__(self):
        self.rollCount = 0

    def roll(self, times):
        result = 0
        for diceroll in range(times):
            self.rollCount += 1
            result += self.rollCount
            if self.rollCount == 100:
                self.rollCount = 0
        return result


def play_practice_game():
    turns = 0
    dicerolls = 0
    while max(player_score[0], player_score[1]) < winning_score:
        rolls = dice.roll(3)
        space = player_space[turns % 2] + rolls

        player_space[turns % 2] = space % 10
        player_score[turns % 2] += player_space[turns % 2]
        dicerolls += 3
        turns += 1
    return dicerolls


def play_real_game(p_score, p_space):
    if p_score[0] >= 21:
        return 1, 0
    if p_score[1] >= 21:
        return 0, 1
    if (p_score[0], p_score[1], p_space[0], p_space[1]) in visited_states:
        return visited_states[(p_score[0], p_score[1], p_space[0], p_space[1])]
    p_wins = (0, 0)
    for roll1 in [1, 2, 3]:
        for roll2 in [1, 2, 3]:
            for roll3 in [1, 2, 3]:
                roll = (roll1 + roll2 + roll3)
                p1_space = (p_space[0] + roll) % 10
                p1_score = p_score[0] + p1_space + 1
                winner = play_real_game([p_score[1], p1_score], [p_space[1], p1_space])
                p_wins = (p_wins[0] + winner[1], p_wins[1] + winner[0])
    visited_states[(p_score[0], p_score[1], p_space[0], p_space[1])] = p_wins
    return p_wins


PART1 = False
dice = Dice()
player_score = (0, 0)
player_space = (1, 7)  # 2, 8
if PART1:
    winning_score = 1000
    dicerolls = play_practice_game()
    print("Player scores: ", player_score)
    print("Dice rolls: ", dicerolls)
    print("Part 1: ", min(player_score[0], player_score[1]) * dicerolls)
else:
    player_wins = [0, 0]
    result = play_real_game(player_score, player_space)
    print("Part 2: player victories: ", result)
    #assert max(result) == 444356092776315
    print("Part 2: ", max(result))

#  Player scores:  [894, 1006]
#  Dice rolls:  1338
#  Part 1:  1196172
#  Part 2:
