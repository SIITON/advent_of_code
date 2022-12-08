data = open('input.txt').read().split("\n")

# Tree is visible if all trees between it and an edge of the grid are shorter than it
# only look up, down, left or right
# The edge is visible
# How many trees are visible from outside the grid?
# +-----> x (cols)
# |
# +---. <-- data[x][y] (visible if the line towards edge is < height)
# V
# y (rows)
visible = {}

edge_width = 1
x_min, x_max = edge_width, len(data[0]) - edge_width
y_min, y_max = edge_width, len(data) - edge_width

vec = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visible_count = 0
render = []
for x in range(len(data)):
    render_line = ''
    for y in range(len(data[0])):
        tree_height = int(data[x][y])
        tree_is_visible = False
        for X, Y in vec:  # For each rotation
            row, col = x, y  # Start position
            visible_from_this_angle = False  # We assume it's not visible
            while True:
                # Move in direction of vector
                row += X
                col += Y
                #  If our next step is not in our data range, we're out -> visible
                if not (0 <= row < len(data) and 0 <= col < len(data[0])):
                    visible_from_this_angle = True
                    break
                neighbor_height = int(data[row][col])
                if neighbor_height >= tree_height:
                    visible_from_this_angle = False
                    break
            if visible_from_this_angle:
                tree_is_visible = True
                break
        if tree_is_visible:
            render_line += '+'
            visible_count += 1
        else:
            render_line += '-'
    render.append(render_line)

for line in render:
    print(line)

# Part 1: Visible trees =  1801
print("Part 1: Visible trees = ", visible_count)
scenic_score = 0
render = []
for x in range(len(data)):
    render_line = ''
    for y in range(len(data[0])):
        tree_height = int(data[x][y])
        tree_score = 1
        for X, Y in vec:  # For each rotation
            row, col = x + X, y + Y  # Start position
            view_distance = 1  # We start by checking a step
            while True:
                #  If our step is not in our data range, we're out of the forest.
                if not (0 <= row < len(data) and 0 <= col < len(data[0])):
                    view_distance -= 1  # We step back and use that distance
                    break
                neighbor_height = int(data[row][col])
                if neighbor_height >= tree_height:  # The view was blocked
                    break
                # Move in direction of vector
                row += X
                col += Y
                view_distance += 1
            tree_score *= view_distance
        scenic_score = max(scenic_score, tree_score)
        if scenic_score == tree_score:
            print("score:", tree_score)
            render_line += '+'
            perfect_spot = (x, y)
        else:
            render_line += '-'

    render.append(render_line)

for line in render:
    print(line)

# Part 2: Scenic score = 209880 at (53, 22)
print("Part 2: Scenic score =", scenic_score, "at", perfect_spot)
