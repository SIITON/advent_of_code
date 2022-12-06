data = open('input.txt').read()

distinct_characters = 14
marker = []
i = 0
while len(marker) < distinct_characters:
    char = data[i]
    marker += [char]
    if len(marker) != len(set(marker)):
        unique = False
        while not unique:
            marker.remove(marker[0])
            unique = len(marker) == len(set(marker))

    i += 1
# Part 1: 1929, Part 2: 3298
print("Part 1/2: ", marker, " at ", i)
