data = open('input.txt').read().split("\n")

# *** Part 1 ***
max_cals = 0
total_elf_cals = 0
for calories in data:
    if calories == '':
        max_cals = max(total_elf_cals, max_cals)
        total_elf_cals = 0
        continue
    total_elf_cals += int(calories)
# Part 1: 66719
print("Part 1: ", max_cals)

# *** Part 2 ***
calories_per_elf = {}
total_elf_cals = 0
elf_num = 0
for calories in data:
    if calories == '':
        calories_per_elf[elf_num] = total_elf_cals
        total_elf_cals = 0
        elf_num += 1
        continue
    total_elf_cals += int(calories)

top3 = sorted(calories_per_elf.values(), reverse=True)[0:3]
# Part 2: Top 3 elfs total:  198551
print("Part 2: ", sum(top3))
