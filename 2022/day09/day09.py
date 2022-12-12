# the head (H) and tail (T) must always be touching
# (diagonally adjacent and even overlapping both count as touching)

# If the head is ever two steps directly up, down, left, or right from the tail,
# the tail must also move one step in that direction so it remains close enough

# Otherwise, if the head and tail aren't touching and aren't in the same row or column,
# the tail always moves one step diagonally to keep up:

# You just need to work out where the tail goes as the head follows a series of motions.
# Assume the head and the tail both start at the same position, overlapping
# --------
# Count all the unique positions the tail visited at least once (len(set(pos_visited)))
import numpy as np
import matplotlib.pyplot as plt


def close_together(h, t):
    touching = False
    if (h == t).all():
        touching = True
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        touching = True
    return touching


def direction_towards(h, t):
    vector = (h - t) / np.linalg.norm(h - t)
    return np.sign(vector)


def print_points(h, t):
    row = []
    for y in range(5):
        line = ''
        for x in range(5):
            if x == h[0] and y == h[1]:
                line += 'H'
            elif x == t[0] and y == t[1]:
                line += 'T'
            else:
                line += '-'
        row.append(line)
    row.reverse()
    for r in row:
        print(r)


# for steps in direction
#   move H
#   if touching, don't move T
#   else, move T

#   A y
#   |
#   +---> x


data = open('input.txt').read().split("\n")
start = np.array((0, 0))
visited_points = {}
visited_points_last_tail = {}
vec = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (x', y') [L, U, R, D]
direction = {'L': vec[0], 'U': vec[1], 'R': vec[2], 'D': vec[3]}
H_pos = start.copy()
T_pos = start.copy()
exT_pos = np.array([start.copy(), start.copy(), start.copy(),
                    start.copy(), start.copy(), start.copy(),
                    start.copy(), start.copy(), start.copy()])
h_visited_x = []
h_visited_y = []
visited_points_x = []
visited_points_y = []
for line in data:
    commands = line.split()
    d_vec = direction[commands[0]]
    steps = int(commands[1])
    #print("== ", commands, "==")
    for step in range(steps):
        # Move H
        H_pos += d_vec
        if not close_together(H_pos, T_pos):
            # Move T towards H
            d = direction_towards(H_pos, T_pos)
            T_pos += np.array([int(d[0]), int(d[1])])
        if not close_together(H_pos, exT_pos[0]):
            # Move T towards H
            d = direction_towards(H_pos, exT_pos[0])
            exT_pos[0] += np.array([int(d[0]), int(d[1])])
        for head in range(len(exT_pos) - 1):
            if not close_together(exT_pos[head], exT_pos[head + 1]):
                d = direction_towards(exT_pos[head], exT_pos[head + 1])
                exT_pos[head + 1] += np.array([int(d[0]), int(d[1])])
        h_visited_x.append(H_pos[0])
        h_visited_y.append(H_pos[1])
        visited_points_x.append(T_pos[0])
        visited_points_y.append(T_pos[1])
        visited_points[(T_pos[0], T_pos[1])] = True
        visited_points_last_tail[(exT_pos[-1][0], exT_pos[-1][1])] = True
        # print_points(H_pos, T_pos)
        # print("--Step--")

visited = len(visited_points)
last_tail_visited = len(visited_points_last_tail)
# Part 1: 5907
# Part 2: 2303
print("Part 1:", visited)
print("Part 2:", last_tail_visited)

fig = plt.figure()
axs = fig.add_subplot()
plt.scatter(x=start[0], y=start[1])
plt.scatter(x=visited_points_x, y=visited_points_y)
# plt.scatter(x=h_visited_x, y=h_visited_y)
plt.legend(["Start", "T"])
axs.set_aspect('equal', adjustable='box')
plt.show()
