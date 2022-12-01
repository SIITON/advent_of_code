import math

data = open('input.txt').read().split("\n")
# The input is 14 similar instructions, different in three commands, by having different values.
# z = z/1 or z/26   (5th command)
# x += unique value (6th command)
# y += unique value (16th command)
"""for instruction in data:
    command = instruction[0:3]
    values = instruction[3:].split()"""

# int(str(W).replace(", ", "").replace("[","").replace("]", ""))
x_add = [12, 11, 14, -6, 15, 12, -9, 14, 14, -5, -9, -5, -2, -7]
z_div = [1, 1, 1, 26, 1, 1, 26, 1, 1, 26, 26, 26, 26, 26]
y_add = [4, 10, 12, 14, 6, 16, 1, 7, 8, 11, 8, 3, 1, 8]


# eql x, w then eql x, 0 -> not_eql x, w
def not_eql(a, b):
    if a == b:
        return 0
    return 1


def first_seven_digits():
    W_ = '9999999'
    z_ = 0
    plausable_w = []
    w_to_z = {}
    done = False
    while not done:
        dividers = 0
        for i in range(7):
            w_ = int(W_[i])
            if x_add[i] < 0:  # When x_add > 9. x is always 1
                #x_ = not_eql(z_ % 26 + x_add[i], w_)
                if z_ % 26 + x_add[i] != w_:
                    break
                """if x_ == 1:  # Not equal to w. x MUST be equal to w otherwise z continues to explode.
                    break"""
                z_ = math.floor(z_/26)
                dividers += 1
            z_ *= 26
            z_ += w_ + y_add[i]
        if dividers == 2:
            plausable_w.append(int(W_))
            w_to_z[int(W_)] = z_
        if W_ == '1111111':
            done = True
        W_ = str(int(W_) - 1)
        while W_.__contains__('0'):
            W_ = str(int(W_) - 1)
        z_ = 0
    plausable_w.sort()
    plausable_w.reverse()
    return plausable_w, w_to_z


def last_seven_digits(w_start, z_start):
    W_ = str(w_start) + '9999999'
    z_ = z_start
    plausible_w = []
    w_to_z = {}
    done = False
    isCorrect = False
    lowest_z = z_start
    while not done:
        dividers = 0
        for i in range(7, 14):
            w_ = int(W_[i])
            if x_add[i] < 0:  # When x_add > 9. x is always 1
                x_ = not_eql(z_ % 26 + x_add[i], w_)
                if x_ == 1:  # Not equal to w. x MUST be equal to w otherwise z continues to explode.
                    break
                z_ = math.floor(z_/26)
                dividers += 1
            z_ *= 26
            z_ += w_ + y_add[i]
        if z_ == 0:
            isCorrect = True
            done = True
            print("W = ", W_, " z = ", z_)
        if dividers == 5:
            plausible_w.append(int(W_))
            w_to_z[int(W_)] = z_
            if z_ == 0:
                isCorrect = True
                done = True
                print("W = ", W_, " z = ", z_)
        if W_ == str(w_start) + '1111111':
            done = True
            break
        W_ = str(int(W_) - 1)
        while W_.__contains__('0'):
            W_ = str(int(W_) - 1)
        if z_ < lowest_z:
            lowest_z = z_
        z_ = 0
    plausible_w.sort()
    plausible_w.reverse()
    return plausible_w, w_to_z, isCorrect, lowest_z


W_first7, w_to_z = first_seven_digits()
print("First sequence done")
possible_initial_z = {}
runs_left = len(W_first7)
#for start_sequence in W_first7:
i = 0
W_first7.reverse()
found_it = False
while not found_it:
    start_sequence = W_first7[i]
    initial_z = w_to_z[start_sequence]
    if possible_initial_z.__contains__(initial_z):
        if not possible_initial_z[initial_z]:
            #print("Ignored ", start_sequence)
            continue
    print("Testing start sequence ", start_sequence)
    print("z = ", w_to_z[start_sequence])
    plausible_w, full_w_to_z, found_it, z_lowest = last_seven_digits(start_sequence, initial_z)
    runs_left -= 1
    i += 1
    """if z_lowest > 100:
        i += 200"""
    print(found_it, "Lowest z: ", z_lowest, " Runs to go: ", runs_left - i)
    if not found_it:
        possible_initial_z[initial_z] = False



#W = '9,' * 13 + '9'
#W = [int(x) for x in W.split(",")]
#int(str(W).replace(", ", "").replace("[","").replace("]", ""))
print("done")


"""W = '99999943472009'
W3 = [6, 7, 8, 9]
runs = 0
# Pattern
z26 = {}
while True: #runs < 3000000:
    x, y, z = [0, 0, 0]
    for i in range(14):
        w = int(W[i])
        if x_add[i] < 0:  # When x_add > 9. x is always 1
            x = not_eql(z % 26 + x_add[i], w)  # z%26 - value != w
            if x != 0:
                # z % 26 + value, must always be equal to w to get z down to 0
                break
            #z /= 26  # z_div[i]
        # x is always 1 here
        #z *= 26  # 25*x + 1
        # y = w + y_add[i]  # *x
        z += w + y_add[i]  # 26*z_old + w + offset
        # z = 26z + w + offset value
    if z == 0:
        break
    #runs += 1
    W = str(int(W) - 1)
print("W: ", W)
print("z: ", z)"""
