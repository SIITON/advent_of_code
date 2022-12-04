import numpy as np


def find_common_value(a, b):
    return [value for value in a if value in b]


data = open('input.txt').read().split("\n")

sections = np.arange(100).tolist()
full_overlap_count = 0
all_overlap_count = 0
for row in data:
    elf_pairs = row.split(',')
    e1 = elf_pairs[0].split('-')
    e2 = elf_pairs[1].split('-')
    e1_0, e1_1 = int(e1[0]), int(e1[1]) + 1
    e2_0, e2_1 = int(e2[0]), int(e2[1]) + 1
    e1_sections = sections[e1_0: e1_1]
    e2_sections = sections[e2_0: e2_1]
    equal_sections = find_common_value(e1_sections, e2_sections)
    if len(equal_sections) == 0:
        continue
    else:
        all_overlap_count += 1
    if len(equal_sections) == len(e1_sections):
        full_overlap_count += 1
        continue
    if len(equal_sections) == len(e2_sections):
        full_overlap_count += 1
# Part 1:  595
print("Part 1: ", full_overlap_count)
# Part 2:  952
print("Part 2: ", all_overlap_count)