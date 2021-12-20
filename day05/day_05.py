import numpy as np
part1 = False


def read_data(data):
    cords_from = np.array([])
    cords_to = np.array([])
    for line in data:
        L = line.split(" ->")
        x_1 = int(L[0].split(",")[0])
        y_1 = int(L[0].split(",")[1])
        x_2 = int(L[1].split(",")[0])
        y_2 = int(L[1].split(",")[1])
        cords_from = np.append(cords_from, [x_1, y_1])
        cords_to = np.append(cords_to, [x_2, y_2])
    return [cords_from, cords_to]


def to_vec2(vec1):
    return vec1.reshape(int(vec1.shape[0] / 2), 2)


def filter(cords_from, cords_to):
    S = np.array([])
    E = np.array([])
    for i in range(cords_from.shape[0]):
        if cords_from[i, 0] == cords_to[i, 0] or cords_from[i, 1] == cords_to[i, 1]:
            S = np.append(S, cords_from[i, :])
            E = np.append(E, cords_to[i, :])
    return S, E


start, end = read_data(open('input.txt').read().split('\n'))
start = to_vec2(start)
end = to_vec2(end)
if part1:
    start, end = filter(start, end)
    start = to_vec2(start)
    end = to_vec2(end)

diagram = np.zeros([int(start.max())+1, int(end.max())+1])
for line in range(start.shape[0]):
    x_1 = int(start[line, 0])
    x_2 = int(end[line, 0])
    y_1 = int(start[line, 1])
    y_2 = int(end[line, 1])
    if x_1 == x_2:
        x = x_1
        for y in range(min(y_1, y_2), max(y_1, y_2) + 1):
            diagram[y, x] += 1
    elif y_1 == y_2:
        y = y_1
        for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
            diagram[y, x] += 1
    else:
        x = x_1
        y = y_1
        diagram[y, x] += 1
        while y != y_2:
            if y_1 < y_2:
                y += 1
            else:
                y -= 1
            if x_1 < x_2:
                x += 1
            else:
                x -= 1
            diagram[y, x] += 1


count = 0
for line in diagram:
    for value in line:
        if value > 1:
            count += 1

print(diagram)
print(count)
#  Part 1: 4745
#  Part 2: 18442
