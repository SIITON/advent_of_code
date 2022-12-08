class Terminal:
    def __init__(self):
        self.data = open('input.txt').read().split("\n")
        self.index = 0

    def read_next(self):
        self.index += 1
        return self.data[self.index - 1]

    def more_data_exists(self):
        return self.index < len(self.data)


class FileSystem:
    def __init__(self):
        self.size_of = {}
        self.path = []
        self.used_space = 0

    def cd(self, position):
        if position == '..':
            self.path.pop()
        elif position == '/':
            self.path = ['/']
        else:
            self.path.append(position)

    def add_item(self, file_size, add_size_to_parents=False):
        size = int(file_size)
        self.used_space += size
        directory = '.'.join(self.path)
        if self.size_of.__contains__(directory):
            self.size_of[directory] += size
        else:
            self.size_of[directory] = size
        if self.not_in_root() and add_size_to_parents:
            self.add_item_size_to_parents_of(directory)

    def not_in_root(self):
        return len(self.path) != 1

    def add_item_size_to_parents_of(self, child: str):
        for p in range(1, len(self.path[:-1])+1):
            directory = '/'.join(self.path[:p])
            if self.size_of.__contains__(directory):
                self.size_of[directory] += self.size_of[child]
            else:
                self.size_of[directory] = self.size_of[child]

    def print(self):
        for path, size in self.size_of.items():
            print("C:", path, "\n\tsize: ", size, )


terminal = Terminal()
filesystem = FileSystem()
# {path: size}
used_space = 0
sz = {}
while terminal.more_data_exists():
    commands = terminal.read_next().split()
    if commands[1] == 'cd':
        filesystem.cd(commands[2])
    elif commands[1] == 'ls':
        continue
    elif commands[0] == 'dir':
        continue
    else:
        used_space += int(commands[0])
        for i in range(1, len(filesystem.path)+1):
            directory = '/'.join(filesystem.path[:i])
            if sz.__contains__(directory):
                sz[directory] += int(commands[0])
            else:
                sz[directory] = int(commands[0])
        filesystem.add_item(commands[0], add_size_to_parents=True)


total_space = 70000000
update_requirement = 30000000
#available_space = total_space - used_space
available_space = total_space - sz['/']  # filesystem.size_of['/']
file_space_needed = update_requirement - available_space
total = 0
smallest_dir = 1e9
print("C: ", filesystem.size_of['/'], "/", total_space, "kb, (", round(100 * (filesystem.size_of['/']/total_space), 1), " %)")
print("Available: ", available_space, "or", total_space - filesystem.used_space, "(", round(100 * (filesystem.used_space/total_space), 1), " %)")
print("Need ", file_space_needed)
folder_size_to_delete = 1e9
total_used = sz['/']
need_to_free = total_used - (total_space - update_requirement)
for path, s in sz.items():  # filesystem.size_of.items
    if s <= 100000:
        total += s
for k, v in sz.items():
    if v >= need_to_free:
        folder_size_to_delete = min(folder_size_to_delete, v)
# Part 1: 1428881
# Part 2: 10,475,598
print("Part 1: ", total)
print("Part 2: ", folder_size_to_delete)
