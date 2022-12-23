# Packet data consists of lists and integers.
# Each list starts with [, ends with ], and contains zero or more comma-separated values (either integers or other lists).
# Each packet is always a list and appears on its own line.

# When comparing two values,
# the first value is called left and the second value is called right.

# If both values are integers, the lower integer should come first.
# If the left integer is lower than the right integer, the inputs are in the right order.

# If the left integer is higher than the right integer,
#   the inputs are not in the right order.
# else, the inputs are the same integer;
# continue checking the next part of the input.

# If both values are lists,
#   for val in list
#   compare the first value of each list,
#   then the second value, and so on.

#If the left list runs out of items first, the inputs are in the right order.
# If the right list runs out of items first, the inputs are not in the right order.
# If the lists are the same length and no comparison makes a decision about the order,
# continue checking the next part of the input.

# If exactly one value is an integer,
# convert the integer to a list which contains that integer as its only value,
# then retry the comparison.
# For example,
# if comparing [0,0,0] and 2,
# convert the right value to [2] (a list containing 2);
# the result is then found by instead comparing [0,0,0] and [2].

# Determine which pairs of packets are already in the right order.
# What is the sum of the indices of those pairs?
import ast
from functools import cmp_to_key
# 1061 points before
# 1125 points after part 1 (64p)
# 1189 points after part 2 (64p)


def compare_two_lists(L:list, R:list):
    i = 0
    while i < len(L) and i < len(R):
        order = compare(L[i], R[i])
        if order != 0:
            return order
        i += 1
    if i == len(L) and i < len(R):  # Left is smaller
        return -1
    elif i < len(L) and i == len(R):  # Right is smaller:
        return 1
    else:  # They're equal
        return 0


def compare_integers(l: int, r: int):
    print("Compare ", l, "vs", r)
    if l == r:
        return 0
    if l < r:
        return -1
    if l > r:
        return 1


# Compare(left, right) returns:
#   1   - left is higher, not in order
#   0   - equal, continue
#  -1   - left is smaller, in order
def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return compare_integers(l, r)
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    elif isinstance(l, list) and isinstance(r, list):
        return compare_two_lists(l, r)


data = open('input.txt').read().split("\n")
sum_of_pairs_in_order = 0
packets = [[[2]], [[6]]]
for i in range(0, len(data) - 1, 3):
    index = i//3 + 1
    print("== Pair", index, "==")
    left = ast.literal_eval(data[i])
    right = ast.literal_eval(data[i + 1])
    packets.append(left)
    packets.append(right)
    print("- Compare ", left, "vs", right)
    in_order = compare(left, right)
    if in_order == 1:
        print("Right is smaller, not in order")
    if in_order == -1:
        print("Left is smaller, in order")
        sum_of_pairs_in_order += index

# Part 2, sort all packets
divider_packets = 1
packets = sorted(packets, key=cmp_to_key(lambda l, r: compare(l, r)))
for i, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        divider_packets *= i+1


# Part 1: 5623
# Part 2: 20570
print("Part 1:", sum_of_pairs_in_order)
print("Part 2:", divider_packets)
