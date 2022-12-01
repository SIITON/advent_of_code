def read_data():
    numbers = data[0].split(',')
    i = 0
    for num in numbers:
        numbers[i] = int(num)
        i += 1
    bingo_boards_data = data[2:]
    boards = []
    for i in range(0, int(len(bingo_boards_data)), 6):
        board = bingo_boards_data[i:6 + i]
        board.pop()
        rows = []
        for row in board:
            val = row.split(' ')
            vals = []
            for num in val:
                if num != '':
                    vals.append(int(num))
            rows.append(vals)
        boards.append(rows)
    return numbers, boards


def check_match(board, value):
    r = 0  # Row
    for rows in board:
        c = 0  # Column
        for val in rows:
            if val == value:
                return True, (r, c)
            c += 1
        r += 1
    return False, (r, c)


def check_bingo(marked_nums):
    diag_sum = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    horiz_sum = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for pos in marked_nums:
        diag_sum[pos[0]] += 1
        horiz_sum[pos[1]] += 1
    for val in diag_sum.values():
        if val == 5:
            return True
    for val in horiz_sum.values():
        if val == 5:
            return True
    return False


# init
data = open('input.txt').read().split("\n")
PART2 = False
numbers, boards = read_data()
# Play bingo, draw numbers
marked_numbers_of_board = {}
is_bingo = False
winning_boards = {}  # index -> bool
for i in range(len(boards)):
    winning_boards[i] = False
for num in numbers:
    done = False
    i = 0
    for board in boards:
        marked_numbers = set()
        match, pos = check_match(board, num)
        if match:
            marked_numbers.add(pos)
            if marked_numbers_of_board.__contains__(i):
                marked_numbers_of_board[i].add(pos)
            else:
                marked_numbers_of_board[i] = marked_numbers
            if len(marked_numbers_of_board[i]) > 5:
                is_bingo = check_bingo(marked_numbers_of_board[i])
                if is_bingo:
                    if not PART2:
                        break
                    winning_boards[i] = True
        winning_boards_count = 0
        for b in winning_boards.values():
            if b:
                winning_boards_count += 1
        if winning_boards_count == len(boards):
            done = True
            break
        i += 1
    if done:
        break
    if is_bingo:
        if not PART2:
            break
if not PART2:
    print("Winning board ", i, " Last number drawn: ", num)
else:
    print("Worst board ", i, " Last number drawn: ", num)
board_score = 0
for line in board:
    for val in line:
        board_score += val
    print(line)
for marked_num in marked_numbers_of_board[i]:
    board_score -= board[marked_num[0]][marked_num[1]]
print("Score: ", board_score * num)
# Part 1:
#   Winning board  75  Last number drawn:  78
#   Score:  55770
# Part 2:
#   Worst board  44  Last number drawn:  10
#   Score:  2980
