
data = open('input.txt').read().split("\n")

total = 0
deck = {}
for i in range(1, len(data) + 1):
    deck[i] = 1
for line in data:
    card_num = int(line.split(':')[0].split()[1])
    print("Let's scratch card #", card_num)
    one_match = 0
    winning_numbers = line.split('|')[0].split()[2:]
    my_numbers = line.split('|')[1].split()
    num_matched = 0
    for num in my_numbers:
        isWinningNum = num in winning_numbers
        if isWinningNum:
            one_match = 1
            print("Matched ", num, " exists in ", winning_numbers)
            num_matched += 1
    print("This card has ", num_matched, " matching numbers")
    num_of_cards = deck[card_num]
    print("I have ", num_of_cards, " copies of this card")
    for i in range(1, num_matched + 1):
        if deck.__contains__(card_num + i):
            print("I get ", num_of_cards, " copies of card ", card_num + i)
            deck[card_num + i] += num_of_cards
        else:
            deck[card_num + i] = num_of_cards
    print(deck)
    total += one_match * 2**(num_matched - 1)

print("Part 1: ", total)
print("Part 2: ", sum(deck.values()))

# Part 1: 23750
# Part 2: 13261850