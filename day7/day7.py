from collections import Counter, defaultdict

card_map = str.maketrans('AKQJT', 'EDCBA')
card_map2 = str.maketrans('AKQJT', 'EDC1A')
hand_type = {'five': 7, 'four': 6, 'fullhouse': 5, 'three': 4, '2pair': 3, 'pair': 2, 'highcard': 1}

class Card:
    def __init__(self, s):
        (a, b) = s.strip().split(' ')
        self.bet = int(b)
        self.cards = a
        self.hand_type = self.determine_hand()
        self.sortkey = self.cards.translate(card_map)

    def determine_hand(self):
        hand = Counter()
        for card in list(self.cards):
            hand[card] += 1

        values = hand.values()

        if 5 in values:
            return hand_type['five']
        elif 4 in values:
            return hand_type['four']
        elif (3 in values) and (2 in values):
            return hand_type['fullhouse']
        elif (3 in values):
            return hand_type['three']
        elif len([x for x in values if x ==2]) == 2:
            return hand_type['2pair']
        elif 2 in values:
            return hand_type['pair']
        else:
            return hand_type['highcard']

    def __lt__(self, other):
        return self.sortkey < other.sortkey
    
    def __str__(self):
        return f'{self.cards} - {self.bet} - {self.sortkey}'
    
    def __repr__(self):
        return f'{self.cards} - {self.bet} - {self.sortkey}'


class Card2(Card):
    def __init__(self, s):
        super().__init__(s)
        self.sortkey = self.cards.translate(card_map2)
        self.hand_type = self.determine_hand()

    def determine_hand(self):
        hand = Counter()
        for card in list(self.cards):
            hand[card] += 1

        values = hand.values()

        if hand['J'] == 0:  # no jacks
            if 5 in values:
                return hand_type['five']
            elif 4 in values:
                return hand_type['four']
            elif (3 in values) and (2 in values):
                return hand_type['fullhouse']
            elif (3 in values):
                return hand_type['three']
            elif len([x for x in values if x ==2]) == 2:
                return hand_type['2pair']
            elif 2 in values:
                return hand_type['pair']
            else:
                return hand_type['highcard']
        else:
            num_jacks = hand['J']
            if 5 in values:
                return hand_type['five']
            elif 4 in values:
                return hand_type['five']
            elif (3 in values) and (2 in values):
                return hand_type['five']
            elif len([x for x in values if x ==2]) == 2:
                if num_jacks == 1:
                    return hand_type['fullhouse']
                else:
                    return hand_type['four']
            elif 3 in values:
                return hand_type['four']
            elif 2 in values:
                return hand_type['three']
            else:
                return hand_type['pair']


def part1():
    cards = defaultdict(list)  # cards grouped by hand type
    with open('input.txt') as fp:
        for line in fp.readlines():
            c = Card(line)
            cards[c.hand_type].append(c)

    for ht in cards.keys():
        cards[ht] = sorted(cards[ht])  # sort lowest hand to highest

    winnings = 0
    hand_number = 1
    for ht in sorted(cards.keys()):  # start from weakest
        for card in cards[ht]:
            print(card)
            winnings += hand_number * card.bet
            hand_number += 1

    print(f'Total winnings is {winnings}')

def part2():
    cards = defaultdict(list)  # cards grouped by hand type
    with open('input.txt') as fp:
        for line in fp.readlines():
            c = Card2(line)
            cards[c.hand_type].append(c)

    for ht in cards.keys():
        cards[ht] = sorted(cards[ht])  # sort lowest hand to highest

    winnings = 0
    hand_number = 1
    for ht in sorted(cards.keys()):  # start from weakest
        for card in cards[ht]:
            print(card, card.hand_type)
            winnings += hand_number * card.bet
            hand_number += 1

    print(f'Total winnings is {winnings}')

part2()