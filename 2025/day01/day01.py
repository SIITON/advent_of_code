class Dial:
    def __init__(self, direction):
        self.direction = direction
        self.number_of_times_pointing_to_zero = 0

    def turn_right(self, number_of_times = 1):
        self.direction = (self.direction + number_of_times) % 100

    def turn_left(self, number_of_times = 1):
        self.direction = (self.direction - number_of_times) % 100

    def stop(self):
        if self.direction == 0:
            self.number_of_times_pointing_to_zero += 1

    def follow_instruction_as_you_were_taught(self, rotation_direction, number_of_turns):
        if rotation_direction == "R":
            self.turn_right(number_of_turns)
        elif rotation_direction == "L":
            self.turn_left(number_of_turns)
        self.stop()

    def use_password_method_0x434c49434b(self, rotation_direction, number_of_turns):
        if rotation_direction == "R":
            for i in range(number_of_turns):
                self.turn_right()
                self.stop()
        elif rotation_direction == "L":
            for i in range(number_of_turns):
                self.turn_left()
                self.stop()


data = open('input.txt').read().split("\n")

firstTry = Dial(50)
for line in data:
    vec = line[0]
    turns = int(line[1:])
    firstTry.follow_instruction_as_you_were_taught(vec, turns)

print("According to your North Pole secret entrance security training seminar")
print("Counts of zeros should be: ", firstTry.number_of_times_pointing_to_zero)

secondTry = Dial(50)
for line in data:
    vec = line[0]
    turns = int(line[1:])
    secondTry.use_password_method_0x434c49434b(vec, turns)

print("\nHowever, by using the password method 0x434C49434B")
print("Counts of zeros should be: ", secondTry.number_of_times_pointing_to_zero)
