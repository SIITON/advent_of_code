def initialize_total(operator: str):
    if operator == '+':
        return 0
    elif operator == '*':
        return 1
    return 0


class Problem:
    def __init__(self, data_input, label):
        s = {}
        i = 0
        self.raw_data = data_input
        for line in data_input:
            s[i] = [s for s in line.split(' ') if s != '']
            i += 1
        self.data = s
        self.label = label
        self.grand_total = 0
        self.operators = self.data[len(self.data) - 1]

    def show(self, title, expected_output = None):
        print(self.label + "\n" + title)
        if expected_output is not None:
            print("Expected", expected_output)
        print("Result", self.grand_total)
        if expected_output is not None:
            print("Difference", expected_output - self.grand_total, "\n")

    def get_values(self, col):
        values = []
        for row in range(len(self.data) - 1):
            value = int(self.data[row][col])
            values.append(value)
        return values

    def solve_part_one(self):
        col = 0
        self.grand_total = 0
        for operator in self.operators:
            col_total = 0
            if operator == '+':
                col_total = 0
            elif operator == '*':
                col_total = 1
            values = self.get_values(col)
            for value in values:
                if operator == '+':
                    col_total += value
                elif operator == '*':
                    col_total *= value
            self.grand_total += col_total
            col += 1

    def solve_part_two(self):
        self.grand_total = 0
        col = len(self.raw_data[0]) - 1
        total_rows_of_data = len(self.raw_data) - 1
        column = len(self.operators) - 1
        operators = self.operators
        operators.reverse()
        for operator in operators:
            col_total = initialize_total(operator)
            column_values = self.get_values(column)
            number_of_values_in_column = len(str(max(column_values)))
            for i in range(number_of_values_in_column):
                value_builder = ""
                for row in range(total_rows_of_data): # 0, 1, 2
                    value_builder += self.raw_data[row][col]
                col_value = int(value_builder)
                if operator == '+':
                    col_total += col_value
                elif operator == '*':
                    col_total *= col_value
                col -= 1
            column -= 1
            col -= 1
            self.grand_total += col_total


data = open('input.txt').read().split('\n')
test_data = open('test.txt').read().split('\\s\n')

test_problem = Problem(test_data, "TEST")
actual_problem = Problem(data, "Uppgift")

test_problem.solve_part_one()
test_problem.show("del 1", 4277556)
test_problem.solve_part_two()
test_problem.show("del 2", 3263827)
actual_problem.solve_part_one()
actual_problem.show("del 1")
actual_problem.solve_part_two()
actual_problem.show("del 2")
