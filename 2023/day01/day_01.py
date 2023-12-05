def try_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 0


def solve_part_one(data):
    total = 0
    for line in data:
        values = []
        for char in line:
            value = try_parse_int(char)
            if value != 0:
                values.append(value)
        first_value = values[0]
        last_value = values[-1]
        combined_value = first_value * 10 + last_value
        total += combined_value
        print("Found ", first_value, " and ", last_value, " | Combined: ", combined_value, " | Total: ", total)

    print("Total: ", total)


def solve_part_two(data):
    total = 0
    line_number = 1
    for line in data:
        values = []
        idx_to_num = {}
        idx = 0
        for char in line:
            value = try_parse_int(char)
            if value != 0:
                values.append(value)
                idx_to_num[idx] = value
            idx += 1
        num_to_idx = {}
        for i in range(1, 10):
            index = line.find(num_to_str[i])
            index_right = line.rfind(num_to_str[i])
            if index != -1:
                num_to_idx[i] = index
                idx_to_num[index] = i
            if index_right != -1:
                num_to_idx[i] = index_right
                idx_to_num[index_right] = i
        # lowest index and highest index
        lowest_index_value = idx_to_num[min(idx_to_num.keys())]
        highest_index_value = idx_to_num[max(idx_to_num.keys())]
        combined_value = lowest_index_value * 10 + highest_index_value
        total += combined_value
        print("Row ", line_number, "Found ", lowest_index_value, " and ", highest_index_value, " | Combined: ",
              combined_value, " | Total: ", total)
        line_number += 1

    print(total)


num_to_str = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

data = open('input.txt').read().split("\n")

solve_part_one(data)
solve_part_two(data)

# Part 1. Total:  55123
# Part 2. Total:  55260
