from collections import defaultdict
from scipy.optimize import minimize_scalar


def read_data(part2=False):
    for line in data:
        monkey = line.split(':')[0]
        job = line.split(':')[1].split()
        if len(job) == 1:  # Just a number
            number_of_monkey[monkey] = int(job[0])
        if len(job) == 3:  # An operation
            monkey_1 = job[0]
            operation = job[1]
            monkey_2 = job[2]
            if part2 and monkey == 'root':
                operation = '-'
            math_operations.add((monkey, monkey_1, operation, monkey_2))


def combine(a, b, operation):
    if operation == '-':
        return a - b
    if operation == '+':
        return a + b
    if operation == '*':
        return a * b
    if operation == '/':
        return a/b
    if operation == '=':
        return a == b


def opposite(operation):
    if operation == '-':
        return '+'
    if operation == '+':
        return '-'
    if operation == '*':
        return '/'
    if operation == '/':
        return '*'


def calculate_part1(verbose=False):
    iter = 0
    while len(math_operations) > 0 or not number_of_monkey.__contains__('root'):
        iter += 1
        if verbose:
            print(iter, 'Number of monkeys with jobs:', len(math_operations))
        for m, m1, o, m2 in math_operations:
            if number_of_monkey.__contains__(m1) and number_of_monkey.__contains__(m2):
                n1 = number_of_monkey[m1]
                n2 = number_of_monkey[m2]
                number = combine(n1, n2, o)
                number_of_monkey[m] = number
                math_operations.remove((m, m1, o, m2))
                break
    return number_of_monkey['root']


def function(verbose=False):
    iter = 0
    while len(math_operations) > 0 or not number_of_monkey.__contains__('root'):
        iter += 1
        if verbose:
            print(iter, 'Number of monkeys with jobs:', len(math_operations))
        for m, m1, o, m2 in math_operations:
            if number_of_monkey.__contains__(m1) and number_of_monkey.__contains__(m2):
                n1 = number_of_monkey[m1]
                n2 = number_of_monkey[m2]
                number = combine(n1, n2, o)
                number_of_monkey[m] = number
                math_operations.remove((m, m1, o, m2))
                break
    return number_of_monkey['humn']


def calculate_part2():
    read_data()
    number_of_monkey.pop('humn')
    operations_to_switch = ['humn']
    while len(operations_to_switch) > 0:
        for m, m1, o, m2 in math_operations:
            if m1 in operations_to_switch:
                # if m = humn + m2
                # then humn = m - m2
                # if (m, m1, o, m2) == (m, H, o, m2) -> add (H, m2, opposite(o), m1)
                operations_to_switch.remove(m1)
                operations_to_switch.append(m2)
                math_operations.remove((m, m1, o, m2))
                math_operations.add((m1, m2, opposite(o), m1))
                break
            if m2 in operations_to_switch:
                # if m = m1 + H
                # then H = m - m1
                # if (m, m1, o, m2) == (m, m1, o, H) -> add (H, m, opposite(o), m1)
                operations_to_switch.remove(m2)
                operations_to_switch.append(m1)
                math_operations.remove((m, m1, o, m2))
                math_operations.add((m2, m, opposite(o), m1))
                break
        print(operations_to_switch)


data = open('input.txt').read().split("\n")
# Points before: 1432
# After part 1: 1509 (77p)
# After part 2:
# Each monkey is given a job:
#   either to yell a specific number or to yell the result of a math operation.

# A lone number means the monkey's job is simply to yell that number.
# A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to yell each of their numbers; the monkey then yells the sum of those two numbers.
# aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
# Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
# Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.
'''        
        if m == 'root' and not rules_set_once:
            if number_of_monkey.__contains__(m1):
                m2_must_be = number_of_monkey[m1]
                number_of_monkey[m2] = m2_must_be
                next_monkey_to_check = m2
                rules_set_once = True
                checked.add((m1, m2))
                break
            if number_of_monkey.__contains__(m2):
                m1_must_be = number_of_monkey[m2]
                number_of_monkey[m1] = m1_must_be
                next_monkey_to_check = m1
                rules_set_once = True
                checked.add((m1, m2))
                break
        elif m1 == next_monkey_to_check or m2 == next_monkey_to_check and (m1, m2) not in checked:
            if number_of_monkey.__contains__(m1):
                m2_must_be = number_of_monkey[m1]
                number_of_monkey[m2] = m2_must_be
                next_monkey_to_check = m2
                checked.add((m1, m2))
            if number_of_monkey.__contains__(m2):
                m1_must_be = number_of_monkey[m2]
                number_of_monkey[m1] = m1_must_be
                next_monkey_to_check = m1
                checked.add((m1, m2))
            break
'''
# What number will the monkey named root yell?

# Parse data input
job_of_monkey = defaultdict()
number_of_monkey = defaultdict()
math_operations = set()
read_data(part2=True)

# Part 1: 160274622817992
#print("Part 1:", calculate_part1())

# PART 2
number_of_monkey.pop('humn')
iter = 0
done = False
rules_set_once = False
next_monkey_to_check = 'root'
checked = set()
#calculate_part2()
'''while len(math_operations) > 0 or not done:
    if number_of_monkey.__contains__('root'):
        if number_of_monkey['root'] == True:
            done = True
    iter += 1
    print(iter, 'Number of monkeys with jobs:', len(math_operations))
    for m, m1, o, m2 in math_operations:
        if number_of_monkey.__contains__(m1) and number_of_monkey.__contains__(m2):
            n1 = number_of_monkey[m1]
            n2 = number_of_monkey[m2]
            if m == 'root':
                number = combine(n1, n2)
            number = combine(n1, n2, o)
            number_of_monkey[m] = number
            math_operations.remove((m, m1, o, m2))
            break'''
read_data()
number_of_monkey.pop('humn')

operations_to_switch = ['humn']
end = ['fflg', 'qwqj']
iter = 0
while iter < 10000:
    to_loop_over = math_operations.copy()
    for m, m1, o, m2 in to_loop_over:
        print("Want to find an equation for", operations_to_switch)
        if m == 'root':
            math_operations.remove((m, m1, o, m2))
            break
        if m == end[0] and m1 in operations_to_switch and number_of_monkey.__contains__(m2):
            # root: fflg == qwqj = True (end[0] & end[1])
            # if
            # maybe fflg = k * z ( m = m1 o m2)
            # now we know qwqj must be a known variable
            # k = m / z, but since m should be equal to end[2]
            # k = qwqj / z
            print("Equation END", m, "=", m1, o, m2)
            print("- Changed to", m1, "=", end[2], o, m2)

            math_operations.remove((m, m1, o, m2))
            math_operations.add((m1, end[2], o, m2))
            operations_to_switch.remove(m1)
            break
        if m == end[0] and m2 in operations_to_switch and number_of_monkey.__contains__(m1):
            print("Equation END", m, "=", m1, o, m2)
            print("- Changed to", m1, "=", end[1], o, m2)
            math_operations.remove((m, m1, o, m2))
            math_operations.add((m1, end[1], o, m2))
            operations_to_switch.remove(m2)
            break
        if m1 in operations_to_switch:
            '''
             We're switching the math operation for monkey m since a is not known anymore
                    m = a + b -> a = b - m
             Then we need to switch math operation that computes m
             m should exist in a chain of operations that leads to the root
                like k = m + n
             Then we switch that one
                to m = k - n
             and the k and so on... til we come to the root
                root = m1 + m2
                maybe m1 = k * z
             now we know m2 must be a known variable
                k = m1 / z, but since m1 should be equal to m2
                k = m2 / z
             if instead m2 = k - l
                k = m2 + l = m1 + l
             Now we can follow the chain as usual and get our answer
            '''
            # if m = m1 + m2 and we should switch m1 and then continue by switching equation that contains m
            # then m1 = m - m2
            # if (m, m1, o, m2) == (m, m1, o, m2) -> add (m1, m2, opposite(o), m)
            print("Equation", m, "=", m1, o, m2)
            print("- Changed to", m1, "=", m2, opposite(o), m)
            operations_to_switch.remove(m1)
            operations_to_switch.append(m)
            math_operations.remove((m, m1, o, m2))
            math_operations.add((m1, m2, opposite(o), m))
            break
        if m2 in operations_to_switch:
            # if m = m1 + H
            # then H = m - m1
            # if (m, m1, o, m2) == (m, m1, o, H) -> add (H, m, opposite(o), m1)
            print("Equation", m, "=", m1, o, m2)
            print("- Changed to", m2, "=", m, opposite(o), m1)
            operations_to_switch.remove(m2)
            operations_to_switch.append(m)
            math_operations.remove((m, m1, o, m2))
            math_operations.add((m2, m, opposite(o), m1))
            break
    print("Total operations left", len(operations_to_switch), operations_to_switch)
    iter += 1
#function()


print("Part 2:", number_of_monkey['humn'])
