def print_test(result:int, expected:int):
    print(result, "\t| RESULT")
    print(expected, "\t| EXPECTED")
    if result == expected:
        print("!! CORRECT !!")
    else:
        print("** INCORRECT ** \t Diff: ", expected - result)


class Manifold:
    def __init__(self):
        self.data = open('input.txt').read().split('\n')
        self.data_test = open('test.txt').read().split('\n')
        self.test_expected_part_1 = 21
        self.test_expected_part_2 = 40

    def test_part_1(self):
        print("****** TEST ******")
        times_the_beam_was_split = self.number_of_times_beam_is_split(is_test=True, verbose=True)
        print_test(times_the_beam_was_split, self.test_expected_part_1)

    def test_part_2(self):
        print("****** TEST ******")
        different_timelines = self.number_of_different_timelines(is_test=True, verbose=True)
        print_test(different_timelines, self.test_expected_part_2)

    def number_of_times_beam_is_split(self, is_test=False, verbose=False):
        data = self.data_test if is_test else self.data
        # Go line by line
        start_pos = data[0].index('S')
        beams_indices = set()
        beams_indices.add(start_pos)
        split_count = 0
        line_to_print = {}
        for line in data[1:]:
            i = 0
            for l in line:
                line_to_print[i] = l
                i += 1
            splitters = self.beam_splitter_indices(line)
            splits = 0
            for splitter in splitters:
                if beams_indices.__contains__(splitter):
                    beams_indices.remove(splitter)
                    beams_indices.add(splitter+1)
                    beams_indices.add(splitter-1)
                    split_count += 1
                    splits += 1
            for splitter in splitters:
                if beams_indices.__contains__(splitter):
                    beams_indices.remove(splitter)
            for beam in beams_indices:
                line_to_print[beam] = '|'
            printable_line = "".join(line_to_print.values())
            if verbose: print(printable_line, "+",splits, "\ttot: ",split_count)

        return split_count

    def number_of_different_timelines(self, is_test=False, verbose=False):
        data = self.data_test if is_test else self.data
        start_pos = data[0].index('S')
        beams_indices = set()
        beams_indices.add(start_pos)
        split_count = 0
        line_to_print = {}
        beam_timelines_by_index = {}
        manifold_width = len(data[0])
        for space in range(manifold_width):
            beam_timelines_by_index[space] = 0
        beam_timelines_by_index[start_pos] = 1
        for line in data[1:]:
            i = 0
            for l in line:
                line_to_print[i] = l
                i += 1
            splitters = self.beam_splitter_indices(line)
            splits = 0
            timelines_added = 0
            timelines_removed = 0
            for splitter in splitters:
                if beams_indices.__contains__(splitter): # If a beam is above a splitter
                    beams_indices.remove(splitter)
                    beams_indices.add(splitter + 1) # Go right
                    beams_indices.add(splitter - 1) # Or go left
                    beam_timelines_by_index[splitter + 1] += beam_timelines_by_index[splitter]
                    beam_timelines_by_index[splitter - 1] += beam_timelines_by_index[splitter]
                    timelines_added += beam_timelines_by_index[splitter]*2
                    timelines_removed = beam_timelines_by_index[splitter]
                    beam_timelines_by_index[splitter] = 0
                    split_count += 1
                    splits += 1
            for splitter in splitters:
                if beams_indices.__contains__(splitter):
                    beams_indices.remove(splitter)
            for beam in beams_indices:
                line_to_print[beam] = '|'
            printable_line = "".join(line_to_print.values())

            if verbose: print(printable_line, "+", timelines_added, "\t-", timelines_removed, "\ttot: ", sum(beam_timelines_by_index.values()))

        return sum(beam_timelines_by_index.values())

    @staticmethod
    def beam_splitter_indices(line):
        i = 0
        splitters = []
        for space in line:
            if space == '^':
                splitters.append(i)
            i += 1
        return splitters


manifold = Manifold()

manifold.test_part_1()
print("With actual input: ", manifold.number_of_times_beam_is_split())

manifold.test_part_2()
print("With actual input: ", manifold.number_of_different_timelines())

# ****** TEST ******
# .......|....... + 0 	tot:  0
# ......|^|...... + 1 	tot:  1
# ......|.|...... + 0 	tot:  1
# .....|^|^|..... + 2 	tot:  3
# .....|.|.|..... + 0 	tot:  3
# ....|^|^|^|.... + 3 	tot:  6
# ....|.|.|.|.... + 0 	tot:  6
# ...|^|^|||^|... + 3 	tot:  9
# ...|.|.|||.|... + 0 	tot:  9
# ..|^|^|||^|^|.. + 4 	tot:  13
# ..|.|.|||.|.|.. + 0 	tot:  13
# .|^|||^||.||^|. + 3 	tot:  16
# .|.|||.||.||.|. + 0 	tot:  16
# |^|^|^|^|^|||^| + 5 	tot:  21
# |.|.|.|.|.|||.| + 0 	tot:  21
# 21 	| RESULT
# 21 	| EXPECTED
# !! CORRECT !!
# With actual input:  1598
# ****** TEST ******
# .......|....... + 0 	- 0 	tot:  1
# ......|^|...... + 2 	- 1 	tot:  2
# ......|.|...... + 0 	- 0 	tot:  2
# .....|^|^|..... + 4 	- 1 	tot:  4
# .....|.|.|..... + 0 	- 0 	tot:  4
# ....|^|^|^|.... + 8 	- 1 	tot:  8
# ....|.|.|.|.... + 0 	- 0 	tot:  8
# ...|^|^|||^|... + 10 	- 1 	tot:  13
# ...|.|.|||.|... + 0 	- 0 	tot:  13
# ..|^|^|||^|^|.. + 14 	- 1 	tot:  20
# ..|.|.|||.|.|.. + 0 	- 0 	tot:  20
# .|^|||^||.||^|. + 12 	- 1 	tot:  26
# .|.|||.||.||.|. + 0 	- 0 	tot:  26
# |^|^|^|^|^|||^| + 28 	- 1 	tot:  40
# |.|.|.|.|.|||.| + 0 	- 0 	tot:  40
# 40 	| RESULT
# 40 	| EXPECTED
# !! CORRECT !!
# With actual input:  4509723641302
