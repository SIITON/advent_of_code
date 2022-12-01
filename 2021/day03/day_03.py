import numpy as np

data = open('input.txt').read().split('\n')

gamma_bin = 0
epsilon_bin = 0

#binary = bin(int(hexdata, 16))[2:]
tally_zeros = np.zeros(len(data[0]))
tally_ones = np.zeros(len(data[0]))
for line in data:
    i = 0
    for bit in line:
        tally_ones[i] += int(bit)
        if bit == '0':
            tally_zeros[i] += 1
        i += 1

gamma = ""
eps = ""
for i in range(len(tally_ones)):
    if tally_ones[i] > tally_zeros[i]:
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"

print(int(gamma, 2))
print(int(eps, 2))
print("power consumption:", int(gamma, 2) * int(eps, 2))
