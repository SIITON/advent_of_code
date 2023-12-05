class Mapper:
    def __init__(self):
        self.range_map = {}
        self.reverse_map = {}

    def setup(self, f, t, r):
        # From this range, to another range
        self.range_map[range(f, f + r)] = range(t, t + r)
        self.reverse_map[range(t, t + r)] = range(f, f + r)

    def map(self, value):
        for input_range in self.range_map:
            if value in input_range:
                low = input_range[0]
                diff = value - low
                return self.range_map[input_range][diff]
        return value

    def map_backwards(self, value):
        for output_range in self.reverse_map:
            if value in output_range:
                low = output_range[0]
                diff = value - low
                return self.reverse_map[output_range][diff]
        return value


def solve_part_one():
    mappings = {}
    for seed in seeds:
        val = int(seed)
        ss = [val]
        for m in mappers:
            val = m.map(val)
            ss.append(val)
        mappings[int(seed)] = val
        print("Seed ", seed, " maps to ", val)
    print(mappings.values())
    print("Min value: ", min(mappings.values()))


data = open('input.txt').read().split("\n")

# destination range start
# source range start
# range length

# Any source numbers that aren't mapped,
# correspond to the same destination number

# find the lowest location number that corresponds to any of the initial seeds

# TOo bIg nUmbErs, use ranges

seeds = data[0].split()[1:]
# seed-to-soil map
s_to_s = Mapper()
# soil-to-fertilizer map
s_to_f = Mapper()
# fertilizer-to-water map
f_to_w = Mapper()
# water-to-light map
w_to_l = Mapper()
# light-to-temperature map
l_to_t = Mapper()
# temperature-to-humidity map
t_to_h = Mapper()
# humidity-to-location map
h_to_l = Mapper()

mappers = [s_to_s, s_to_f, f_to_w, w_to_l, l_to_t, t_to_h, h_to_l]
i = 0
for line in data[2:]:
    if line == '':
        # new mapper
        i += 1
        continue
    if line[-1] == ':':
        continue
    mapper = mappers[i]
    values = line.split()
    fr = int(values[1])
    to = int(values[0])
    r = int(values[2])
    mapper.setup(fr, to, r)

print("Setup complete")

solve_part_one()

print("Starting part 2")
seed_ranges = []
for i in range(0, len(seeds), 2):
    low = int(seeds[i])
    high = low + int(seeds[i + 1])
    seed_ranges.append(range(low, high))

reversed_mappers = mappers.copy()
reversed_mappers.reverse()

# 0 - 5000000           done
#  5000000 - 10000000   done
# 10000000 - 20000000   done
# 20000000 - 30000000   done
# 30000000 - 40000000   done
# 40000000 - 50000000   done
# 50000000 - 60000000   done
# 60000000 - 70000000   done
# 70000000 - 80000000   done found 78775051

i = 78775050
print("Starting brute force at i = ", i)
while i < 80000000:
    val = i
    for m in reversed_mappers:
        val = m.map_backwards(val)
    for j in range(seed_ranges.__len__()):
        if val in seed_ranges[j]:
            print("found seed = ", val, " location = ", i)
            i = 999999999999
            break
    i += 1

# Part 1: 227653707
# Part 2: 78775051
