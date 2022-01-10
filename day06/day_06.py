
def test_values(trueValues):
    i = 0
    test = []
    for val in timers.timers.values():
        test.append(val)
    print(test)
    print(trueValues)
    print(test == trueValues)


class Counter:
    def __init__(self):
        self.count = 0
        self.timers = {}
        for days in range(8 + 1):
            self.timers[days] = 0
        for startVal in data:
            if self.timers.__contains__(int(startVal)):
                self.timers[int(startVal)] += 1
            else:
                self.timers[int(startVal)] = 1
        self.sum_of_lanternfish()

    def sum_of_lanternfish(self):
        count = 0
        for counts in self.timers.values():
            count += counts
        self.count = count
        return self.count

    def copy_dict(self):
        i = 0
        new_dict = {}
        for val in self.timers.values():
            new_dict[i] = val
            i += 1
        return new_dict

    def step(self):
        # each fish creates one new every 7 days
        # a new fish need slightly longer before producing fish
        #   two extra days for its first cycle
        # 3 -> 2 -> 1 -> 0 -> 6 and 8 -> 5 and 7
        copy_timer = self.copy_dict()
        for daysUntilNew in range(8, -1, -1):  # 0, 1,...,8
            next_day = (daysUntilNew - 1) % 9
            if daysUntilNew == 0:
                self.timers[6] += copy_timer[0]
                self.timers[8] = copy_timer[0]
            else:
                self.timers[next_day] = copy_timer[daysUntilNew]


data = open('input.txt').read().split(",")
#data = [3, 4, 3, 1, 2] # small test input
timers = Counter()

for days in range(256):
    timers.step()
    print("Step ", days + 1, " Lanternfish: ", timers.sum_of_lanternfish())

# Step  80   Lanternfish:  362639
# Step  256  Lanternfish:  1639854996917

'''
# Test 0 step
test_values([0, 1, 1, 2, 1, 0, 0, 0, 0])
# Test 1 step
test_values([1, 1, 2, 1, 0, 0, 0, 0, 0])
timers.step()
# Test 2 step
test_values([1, 2, 1, 0, 0, 0, 1, 0, 1])
'''
