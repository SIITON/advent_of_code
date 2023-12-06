def calc_distance(velocity, time_remaining):
    return velocity * time_remaining


def solve_part_one():
    times = data[0].split()[1:]
    dists = data[1].split()[1:]
    total_wins = 1
    for race in range(len(times)):
        t = int(times[race])
        d = int(dists[race])
        print("Race #", race, " Target time is ", t, " Distance to win: ", d)
        wins = 0
        for acc_time in range(t):
            # Hold button
            dist = calc_distance(acc_time, t - acc_time)
            if dist > d:
                # print("Hold the button for ", acc_time, " with the remaining ", t - acc_time, " s. We will travel ", dist)
                wins += 1
        if wins != 0:
            total_wins *= wins
    print(total_wins)
    return total_wins


def solve_part_two():
    t = int(data[0].split(':')[1].replace(" ", ""))
    d = int(data[1].split(':')[1].replace(" ", ""))
    total_wins = 1

    print("Target time is ", t, " Distance to win: ", d)
    wins = 0
    for acc_time in range(t):
        # Hold button
        dist = calc_distance(acc_time, t - acc_time)
        if dist > d:
            # print("Hold the button for ", acc_time, " with the remaining ", t - acc_time, " s. We will travel ", dist)
            wins += 1
    if wins != 0:
        total_wins *= wins
    print(total_wins)

data = open('input.txt').read().split("\n")

# Determine the number of ways you could beat the record in each race.
# What do you get if you multiply these numbers together?
# Test result 4 * 8 * 9 = 288

# Boats move faster if their button was held longer,
# but time spent holding the button counts against the total race time.
# You can only hold the button at the start of the race,
# and boats don't move until the button is released.

solve_part_one()
solve_part_two()

# Part 1: 588588
# Part 2: 34655848
