
# (x, y, z)
# on/off x=x0..xn, y=y0..yn, z=z0..zn


def read_data(data, limit):
    state = []
    x = []
    y = []
    z = []
    for line in data:
        info = line.split()
        cords = info[1].split(",")
        x_interval = cords[0].replace("x=", "").split("..")
        if not (-limit <= int(x_interval[0]) <= limit):
            continue
        if info[0] == "on":
            state.append(True)
        if info[0] == "off":
            state.append(False)
        x.append((int(x_interval[0]), int(x_interval[1])))
        y_interval = cords[1].replace("y=", "").split("..")
        y.append((int(y_interval[0]), int(y_interval[1])))
        z_interval = cords[2].replace("z=", "").split("..")
        z.append((int(z_interval[0]), int(z_interval[1])))
    return state, x, y, z


def part1_count():
    s, x, y, z = read_data(data, 50)
    # Test
    '''
    x = [(10, 12), (11, 13), (9, 11), (10, 10)]
    y = [(10, 12), (11, 13), (9, 11), (10, 10)]
    z = [(10, 12), (11, 13), (9, 11), (10, 10)]
    s = [True, True, False, True]
    '''
    lit_cubes = {}
    for i in range(len(s)):
        for cube_x in range(min(x[i]), max(x[i]) + 1):
            for cube_y in range(min(y[i]), max(y[i]) + 1):
                for cube_z in range(min(z[i]), max(z[i]) + 1):
                    lit_cubes[(cube_x, cube_y, cube_z)] = s[i]
        print("Step ", i, " Cubes lit: ", len(lit_cubes.values()))
    count = 0
    for cube in lit_cubes:
        if lit_cubes[cube]:
            count += 1
    return count


def part2_count():
    s, x, y, z = read_data(data, 1000000)
    # Think volume, not voxels!
    # Lengths, not ranges. But how?
    lit_cubes = set()
    for i in range(len(s)):
        x0, xn = min(x[i]), max(x[i]) + 1
        y0, yn = min(y[i]), max(y[i]) + 1
        z0, zn = min(z[i]), max(z[i]) + 1
        #count2 += (abs(min(x[i])) + abs(max(x[i])) +1) * (abs(min(y[i])) + abs(max(y[i]))+1) * (abs(min(z[i])) + abs(max(z[i]))+1)
        for cube_x in range(x0, xn):
            for cube_y in range(y0, yn):
                for cube_z in range(z0, zn):
                    if s[i]:
                        lit_cubes.add((cube_x, cube_y, cube_z))
                    else:
                        lit_cubes.discard((cube_x, cube_y, cube_z))
        print("Step ", i, " Cubes lit: ", len(lit_cubes))
    count = len(lit_cubes)
    return count

Part1 = False
data = open('test.txt').read().split('\n')
if Part1:
    c = part1_count()
    print("Num of cubes lit: ", c)
    # 602574
else:
    c = part2_count()
    print("Num of cubes lit: ", c)


