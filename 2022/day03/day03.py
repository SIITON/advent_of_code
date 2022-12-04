def find_common_value(a, b):
    return [value for value in a if value in b]


def find_common_value_in(group):
    return find_common_value(find_common_value(group[0], group[1]), group[2])


data = open('input.txt').read().split("\n")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total_priority = 0
for rucksack in data:
    first_compartment = rucksack[0:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]
    common_value = find_common_value(first_compartment, second_compartment)[0]
    total_priority += alphabet.index(common_value) + 1

# Part 1:  8349
print("Part 1: ", total_priority)

total_priority = 0
for i in range(len(data)//6):
    p = 6*i
    group_one = data[p: p + 3]
    group_two = data[p + 3: p + 6]
    common_value_in_group_one = find_common_value_in(group_one)[0]
    common_value_in_group_two = find_common_value_in(group_two)[0]
    total_priority += alphabet.index(common_value_in_group_one) + 1
    total_priority += alphabet.index(common_value_in_group_two) + 1

# Part 2:  2681
print("Part 2: ", total_priority)

