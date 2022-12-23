# Points before: 1189
# After part 1: 1279 (90p)
# After part 2:

# sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance

# In the row where y=2000000, how many positions cannot contain a beacon?
#
# There can't be any other beacons (B) in the radius (r) around the sensor (S)
#          _____
#        /       \
#       |--r-S    B
#        \       /
#         \ ___ /
# Since it's manhattan distance: Distance = 3. Radius is in the form of a rectangle
#       . . . . # . . . .   +-----> x (width/cols)
#       . . . # # B . . .   |
#       . . # # # # # . .   |   * <-- (x, y)
#       . # # # S # # # .   V
#       . . # # # # # . .   y (depth/rows)
#       . . . # # # . . .
#       . . . . # . . . .
#
import numpy as np


def distance(p, q):
    return np.abs(p-q).sum()


data = open('input.txt').read().split("\n")
sensors = set()
beacons = set()
for row in data:
    line = row.split(':')
    sensor_reading = line[0].replace('Sensor at ', '')
    sensor_x = int(sensor_reading.split(',')[0].replace('x=', ''))
    sensor_y = int(sensor_reading.split(',')[1].replace('y=', ''))
    beacon_reading = line[1].replace(' closest beacon is at ', '')
    beacon_x = int(beacon_reading.split(',')[0].replace('x=', ''))
    beacon_y = int(beacon_reading.split(',')[1].replace('y=', ''))
    S = np.array([sensor_x, sensor_y])
    B = np.array([beacon_x, beacon_y])
    dist = distance(S, B)
    sensors.add((sensor_x, sensor_y, dist))
    beacons.add((beacon_x, beacon_y))

depth = 2000000  # Test: 10 | Part 1: 2000000
count = 0
steps = 0
x = -700000
while x <= 4600000:
    p = np.array([x, depth])
    p_is_not_a_beacon = False
    for (sx, sy, d) in sensors:
        if distance(p, [sx, sy]) <= d and (p[0], p[1]) not in beacons:  # Point is close to a sensor -> not a beacon
            p_is_not_a_beacon = True
    if p_is_not_a_beacon:
        count += 1
    steps += 1
    x += 1
    if np.mod(steps, 100000) == 0:
        progress = steps/(4600000 + 700000 + 1)
        print(100*progress, "% (x=", x, "). Positions not in beacons:", count)

#Part 1: 5147333
print("Part 1:", count)
