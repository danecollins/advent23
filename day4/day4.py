import re
from collections import Counter
import pdb


test = 'Card   1: 13  4 61 82 80 41 31 53 50  2 | 38 89 26 79 94 50  2 74 31 92 80 41 13 97 61 82 68 45 64 39  4 53 90 84 54'

pat = re.compile('\d+')

m = {0: 0, 1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256, 10: 512, 11: 1024}

def part1():
    win_sum = 0

    with open('input.txt') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            (x, y) = line.split(':')
            card_number = int(x[4:])
            (winning, have) = y.split('|')
            winning = pat.findall(winning)
            have = pat.findall(have)
            matches = [x for x in have if x in winning]
            win_sum += m[len(matches)]
    
    print(f'Part 1 win sum {win_sum}')


def part2():
    card_sum = 0
    cards = Counter()  # each card has one default card

    with open('input.txt') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            (x, y) = line.split(':')
            card_number = int(x[4:])
            cards[card_number] += 1  # add the current card
            print(f'Card number = {card_number}')
            (winning, have) = y.split('|')
            winning = pat.findall(winning)
            have = pat.findall(have)
            matches = [x for x in have if x in winning]
            print(f'Matches = {len(matches)}')
            # for each match increment the future cards by one
            for x in range(card_number+1, card_number + 1 + len(matches)):
                cards[x] += cards[card_number]
                print(f'   cards[{x}] = {cards[x]}')
            
    card_sum = sum([v for v in cards.values()])
    for k, v in cards.items():
        print(f'Card {k} = {v}')
    print(f'Part 2 card sum {card_sum}')  

part2()