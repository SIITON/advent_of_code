CYEL = '\033[93m'
CEND = '\33[0m'


class Octopuses:
    """
    +----> col, y
    |
    v
    row, x
"""
    def __init__(self, input_path, verbose=False, part=1):
        data = open(input_path).read().split("\n")
        self.verbose = verbose
        self.part = part
        self.steps = 0
        self.energy = {}
        self.flashed_this_step = {}
        x, y = [0, 0]
        for rows in data:
            y = 0
            for cols in rows:
                self.energy[(x, y)] = int(cols)
                self.flashed_this_step[(x, y)] = False
                y += 1
            x += 1
        self.flash_reset = self.flashed_this_step.copy()
        self.new_energy = self.energy.copy()
        self.flashes = 0
        self.all_flashing = False
        if self.verbose:
            print("Initial")
            self.print_energy()

    def print_energy(self):
        print("---------- step ", self.steps)
        for x in range(10):
            line = ""
            for y in range(10):
                if self.energy[(x, y)] == 0:
                    line += CYEL + str(self.energy[(x, y)]) + CEND
                else:
                    line += str(self.energy[(x, y)])
            print(line)

    def step(self):
        previous_energy = self.energy.copy()
        self.steps += 1
        # Increase energy level
        self.increase_energy_level_by_one()
        self.new_energy = self.energy.copy()
        self.check_and_flash()
        self.energy = self.new_energy.copy()
        self.flashes += self.count_flashes()
        # Set all flashed octopuses to 0, reset
        self.reset()
        if self.verbose:
            self.print_energy()

    def reset(self):
        for cords in self.energy.keys():
            if self.flashed_this_step[cords]:
                self.energy[cords] = 0
        self.flashed_this_step = self.flash_reset.copy()

    def count_flashes(self):
        count = 0
        for flashed in self.flashed_this_step.values():
            if flashed:
                count += 1
        if count == 100 and self.part == 2:
            self.all_flashing = True
        return count

    def check_and_flash(self):
        for x in range(10):
            for y in range(10):
                if self.new_energy[(x, y)] > 9 and not self.flashed_this_step[(x, y)]:
                    # FLASH!
                    self.flashed_this_step[(x, y)] = True
                    self.increase_adjacent_by_one((x, y))
                    self.check_and_flash()
    '''  
     (x-1, y-1)  (x-1, y)  (x-1, y+1)        [-1, -1, -1]        [-1, 0, 1]
     (x, y-1)     (x, y)    (x, y+1)    x_ = [ 0,  0,  0]   y_ = [-1, 0, 1]
     (x+1, y-1)  (x+1, y)  (x+1, y+1)        [ 1,  1,  1]        [-1, 0, 1]
    '''
    def increase_adjacent_by_one(self, cord):
        x_ = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        y_ = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        x, y = [cord[0], cord[1]]
        for i in range(9):
            if x + x_[i] < 0 or x + x_[i] > 9:
                continue
            if y + y_[i] < 0 or y + y_[i] > 9:
                continue
            self.new_energy[(x + x_[i], y + y_[i])] += 1

    def increase_energy_level_by_one(self):
        for cord in self.energy.keys():
            self.energy[cord] += 1


# init
octopuses = Octopuses(input_path='input.txt', verbose=True, part=2)
steps = 2000
for step in range(steps):
    octopuses.step()
    print("Flashes: ", octopuses.flashes)
    if octopuses.all_flashing:
        break
# Part 1: 1697
# Part 2: 344
