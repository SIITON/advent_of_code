data = open('input.txt').read().split("\n")
PART = 2
CrateMoverModel = 9000
if PART == 2:
    CrateMoverModel = 9001

stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for line in reversed(data[0:8]):
    for i in range(9):
        crate = line[4 * i + 1]
        if crate != ' ':
            stacks[i+1] += crate
    print(line)

for instruction in data[10:]:
    amount_to_move = int(instruction[5:7])
    from_stack = int(instruction[12:14])
    to_stack = int(instruction[17:19])
    if CrateMoverModel == 9000:
        for moves in range(amount_to_move):
            crate = stacks[from_stack].pop()
            stacks[to_stack] += crate
    if CrateMoverModel == 9001:
        crates = stacks[from_stack][-amount_to_move:]
        stacks[to_stack] += crates
        for moves in range(amount_to_move):
            stacks[from_stack].pop()

result = ''
for stack in stacks.values():
    result += stack[-1]
print(result)
