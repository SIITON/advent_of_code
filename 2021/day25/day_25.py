import numpy as np
data = open('input.txt').read().split('\n')
# ..>>.. then ..>.>. then ...>.> then >...>. (!)
# If anything is in the way, stay still, else move
# [x, y]
#  +---> y
#  |  (0,0)   (0, 1)   (0, 2) ... (0, 138)
#  V  (1,0)   (1, 1)   (1, 2)
#  x  (2,0)   (2, 1)   (2, 2)
#       .
#       .
#    (136, 0)
# Find the number of steps until they stop moving.


def count_cucumbers(data):
    easts = 0
    souths = 0
    for line in data:
        for pos in line:
            if pos == '>':
                easts += 1
            if pos == 'v':
                souths += 1
    return easts, souths


def plot_cucumbers(input):
    text = ""
    for arr in input:
        line = ""
        for pos in arr:
            if pos == '.':
                line += '´'
            else:
                line += pos
        text += line + "\n"
    print(text, flush=True)


x_range = len(data)
y_range = len(data[0])
dots = np.repeat('.', y_range)
cleanSlate = np.repeat(dots, x_range)
cleanSlate.resize(x_range, y_range)
isMoving = True
steps = 0
cucumbers = count_cucumbers(data)
print("Step ", steps)
print("Cucumbers [ > , v ]: ", count_cucumbers(data))
while isMoving:
    movingCucumbers = 0
    #plot_cucumbers(data)
    steps += 1
    new_data = np.array(cleanSlate)
    # east facing moves first
    for x in range(x_range - 1, -1, -1):
        for y in range(y_range - 1, -1, -1):
            pos = data[x][y]
            if data[x][y] == '>':
                # Check to the right
                if data[x][(y+1) % y_range] == '.':
                    new_data[x][(y+1) % y_range] = '>'
                    movingCucumbers += 1
                else:
                    new_data[x][y] = '>'
    # south facing goes second
    for x in range(x_range):
        for y in range(y_range):
            pos = data[x][y]
            if data[x][y] == 'v':
                # Check down
                if data[(x+1) % x_range][y] != 'v' and new_data[(x+1) % x_range][y] == '.':
                    new_data[(x+1) % x_range][y] = 'v'
                    movingCucumbers += 1
                else:
                    new_data[x][y] = 'v'

    print("Step ", steps, "Moving: ", movingCucumbers)
    data = np.array(new_data)
    #print("Cucumbers [ > , v ]: ", count_cucumbers(data))
    isMoving = movingCucumbers > 0

print("Sea cucumbers stop moving after ", steps, " steps")
# Sea cucumbers stop moving after  601  steps
