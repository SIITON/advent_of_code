def is_even(num):
    return num % 2 == 0

class ProductIds:
    def __init__(self, product_id_range:str):
        range_of_ids = product_id_range.split('-')
        self.first = int(range_of_ids[0])
        self.last = int(range_of_ids[1])

    def get_invalid_ids(self):
        if is_even(len(str(self.first))):
            size = int(len(str(self.first))/2)
        else:
            size = int(len(str(self.last))/2)
        for i in range(self.first, self.last+1):
            string = str(i)
            first_half = string[:size]
            second_half = string[size:]
            if first_half == second_half:
                yield i


class Scanner:
    def __init__(self, product_id_range:list[str]):
        self.products = []
        for id_range in product_id_range:
            product = ProductIds(id_range)
            self.products.append(product)

        self.total = 0
        for product in self.products:
            invalid_ids = product.get_invalid_ids()
            for invalid_id in invalid_ids:
                self.total += invalid_id

    def sum_invalid_ids(self):
        return self.total


data = open('input.txt').read().split(',')
test_data = open('test.txt').read().split(',')
test_result = 1227775554

test = Scanner(test_data)
print("Test, expected", test_result)
print("Test, actual", test.sum_invalid_ids())
print("Difference", test.sum_invalid_ids() - test_result)


part1 = Scanner(data)
print("Part 1 result", part1.sum_invalid_ids())