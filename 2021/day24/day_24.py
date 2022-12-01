import sys

data = open('input.txt').read().split("\n")
"""
The ALU is a four-dimensional processing unit: it has integer variables w, x, y, and z. 
These variables all start with the value 0. 
The ALU also supports six instructions:
    inp a - Read an input value and write it to variable a.
    add a b - Add the value of a to the value of b, then store the result in variable a.
    mul a b - Multiply the value of a by the value of b, then store the result in variable a.
    div a b - Divide the value of a by the value of b, 
              truncate the result to an integer, 
              then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
    mod a b - Divide the value of a by the value of b, 
              then store the remainder in variable a. (This is also called the modulo operation.)
    eql a b - If the value of a and b are equal, then store the value 1 in variable a. 
              Otherwise, store the value 0 in variable a.
"""


class Alu:
    def __init__(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.index = 0
        self.model_number = [1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9]

    def reset(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.index = 0

    def set_model_number(self, array):
        if len(array) == 14:
            self.model_number = array
        else:
            print("Wrong array size: ", len(array))

    def inp(self, variable):
        self.set(variable, self.model_number[self.index])
        self.index += 1

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def mod(self, a, b):
        return a % b

    def eql(self, a, b):
        val = 0
        if a == b:
            val = 1
        return val

    def set(self, variable, value):
        if variable == 'w':
            self.w = value
        elif variable == 'x':
            self.x = value
        elif variable == 'y':
            self.y = value
        elif variable == 'z':
            self.z = value

    def get(self, variable):
        if variable == 'w':
            return self.w
        if variable == 'x':
            return self.x
        if variable == 'y':
            return self.y
        if variable == 'z':
            return self.z
        return int(variable)

    def run(self, command, values):
        if command == "inp":  # Read an input value and write it to the variable in values[0]
            var = values[0]
            self.inp(var)
        elif command == "add":
            a = self.get(values[0])
            b = self.get(values[1])
            if b == 0:
                return
            val = self.add(a, b)
            self.set(values[0], val)
        elif command == "mul":
            a = self.get(values[0])
            b = self.get(values[1])
            val = self.mul(a, b)
            self.set(values[0], val)
        elif command == "div":
            a = self.get(values[0])
            b = self.get(values[1])
            val = self.div(a, b)
            self.set(values[0], val)
        elif command == "mod":
            a = self.get(values[0])
            b = self.get(values[1])
            val = self.mod(a, b)
            self.set(values[0], val)
        elif command == "eql":
            a = self.get(values[0])
            b = self.get(values[1])
            val = self.eql(a, b)
            self.set(values[0], val)


def not_eql(a, b):
    if a == b:
        return 0
    return 1


#alu = Alu()
# Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# nope
x_add = [12, 11, 14, -6, 15, 12, -9, 14, 14, -5, -9, -5, -2, -7]
z_div = [1, 1, 1, 26, 1, 1, 26, 1, 1, 26, 26, 26, 26, 26]
y_add = [4, 10, 12, 14, 6, 16, 1, 7, 8, 11, 8, 3, 1, 8]
for _1 in range(9, 0, -1):
    for _2 in range(9, 0, -1):
        for _3 in range(9, 0, -1):
            for _4 in range(9, 0, -1):
                for _5 in range(9, 0, -1):
                    for _6 in range(9, 0, -1):
                        for _7 in range(9, 0, -1):
                            for _8 in range(9, 0, -1):
                                for _9 in range(9, 0, -1):
                                    for _10 in range(9, 0, -1):
                                        for _11 in range(9, 0, -1):
                                            for _12 in range(9, 0, -1):
                                                for _13 in range(9, 0, -1):
                                                    for _14 in range(9, 0, -1):
                                                        W = [_1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14]
                                                        x, y, z = [0, 0, 0]
                                                        for i in range(14):
                                                            w = W[i]
                                                            if x_add[i] < 0:
                                                                x = not_eql(z % 26 + x_add[i], w)
                                                                if x != 0:
                                                                    break
                                                                z /= 26
                                                            z *= 26
                                                            z += w + y_add[i]
                                                        if z == 0:
                                                            print(W)
                                                            sys.exit()
                                                        """alu.set_model_number(number)
                                                        for instruction in data:
                                                            command = instruction[0:3]
                                                            values = instruction[3:].split()
                                                            alu.run(command, values)
                                                        if alu.z == 0:
                                                            print(number)
                                                            break
                                                        alu.reset()"""

"""print("w: ", alu.w)
print("x: ", alu.x)
print("y: ", alu.y)
print("z: ", alu.z)"""
