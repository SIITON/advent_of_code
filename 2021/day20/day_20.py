import numpy as np

data = open('input.txt').read().split('\n')

enhancement_string = data[0]
input_img = data[2:]
x_diff = np.array([-1, -1, -1, 0, 0, 0, 1, 1, 1])
y_diff = np.array([-1, 0, 1, -1, 0, 1, -1, 0, 1])
finite_range = 10


def to_binary(input_string):
    binary = input_string.replace(".", "0").replace("#", "1")
    return int(binary, 2)


def enhance(image):
    new_image = np.array([])
    for row in range(-finite_range, len(image) + finite_range):
        new_row = ""
        for col in range(-finite_range, len(image[0]) + finite_range):
            pixel = ""
            for i in range(len(x_diff)):
                #  if outside the image, it's a .
                x = row + x_diff[i]
                y = col + y_diff[i]
                if x < 0 or x > len(image) - 1:
                    pixel += "."
                elif y < 0 or y > len(image[0]) - 1:
                    pixel += "."
                else:
                    pixel += image[x][y]
            reading = to_binary(pixel)
            new_pixel = enhancement_string[reading]
            new_row += new_pixel
        new_image = np.append(new_image, new_row)
    return new_image


def count_lit_pixels(image):
    count = 0
    for row in image:
        for pixel in range(len(row)):
            if row[pixel] == "#":
                count += 1
    return count

#  Part 2
old_image = input_img
for times_to_enhance in range(25):
    print(times_to_enhance*2 + 1)
    enhanced_img = enhance(enhance(old_image))
    cut_topbot = enhanced_img[1:-finite_range][finite_range:-1]
    old_image = np.array([])
    for i in range(len(cut_topbot)):
        old_image = np.append(old_image, cut_topbot[i][finite_range:-finite_range - 1])

# Part 1
#enhanced_img = enhance(enhance(input_img))

# Part 1 & 2
count = 0
cut_topbot = enhanced_img[1:-finite_range][finite_range:-1]
for i in range(len(cut_topbot)):
    count += count_lit_pixels(cut_topbot[i][finite_range:-finite_range - 1])

print(enhanced_img)
print(" Num of lit pixels: ", count)
#  Part 1: 5461
#  Part 2: 18226
