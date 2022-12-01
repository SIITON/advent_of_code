data = open('input.txt').read().split('\n')
#data = open('testinput.txt').read().split('\n')

pos = 0
depth = 0
aim = 0
for command in data:
    value = int(command[-1])
    if command[0] == 'f':
        pos += value          # forward X increases the horizontal position by X units.
        depth += aim * value  # increases your depth by your aim multiplied by X.
    if command[0] == 'd':
        #  depth += value  # Part1: down X increases the depth by X units.
        aim += value    # down X increases your aim by X units.
    if command[0] == 'u':
        #  depth -= value  # Part1: up X decreases the depth by X units.
        aim -= value    # up X decreases your aim by X units.

print(pos*depth)
