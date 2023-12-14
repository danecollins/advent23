import re
import pdb
from collections import defaultdict

def rng(start, len):
    return range(start, start+len)


class PartNumber:
    value = None
    row = 0
    start_col = 0
    len = 0
    
    def __init__(self, v, s, r):
        self.value = int(v)
        self.start_col = s
        self.len = len(str(v))
        self.row = r
        assert self.value > 0
            

    def generate_adjacent(self):
        adj_pairs = []
        for row in rng(self.row - 1,3):
            for col in rng(self.start_col - 1, self.len+2):
                adj_pairs.append((row, col))
        return adj_pairs
    
    def __str__(self):
        return f'R={self.row}\tV={self.value}\tC={self.start_col}'

def collect_symbols(filename='input.txt'):
    symbol_locations = []
    valid_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    with open(filename) as fp:
        row = 0
        for line in fp.readlines():
            line = line.rstrip()
            row += 1
            chars = list(line)  # convert to character array
            for col, char in zip(rng(1, len(chars)), chars):
                if char not in valid_list:
                    symbol_locations.append((row, col))
    return symbol_locations


def collect_gears(filename='input.txt'):
    gear_locations = []
    gear_list = ['*']
    with open(filename) as fp:
        row = 0
        for line in fp.readlines():
            line = line.rstrip()
            row += 1
            chars = list(line)  # convert to character array
            for col, char in zip(rng(1, len(chars)), chars):
                if char not in gear_list:
                    gear_locations.append((row, col))
    return gear_locations


def get_part_numbers(row, s):
    p = re.compile(r'(\d+)')
    pns = []

    start_col = 0
    for num in p.findall(s):
        col = s.find(num, start_col)
        pns.append(PartNumber(num, col+1, row))
        start_col = col + len(num)
    return pns


def part1():
    sym_loc = collect_symbols()
    sym_loc = set(sym_loc)
    part_numbers = []


    with open('input.txt') as fp:
        row = 0
        pns = []
        for line in fp.readlines():
            line = line.rstrip()
            row += 1
            part_numbers += get_part_numbers(row, line)

    valid_part_numbers = []
    for pn in part_numbers:
        tmp = set(pn.generate_adjacent()) & sym_loc
        if tmp:
            valid_part_numbers.append(pn)

    total = sum([x.value for x in valid_part_numbers])
    print(total)

def part2():
    gear_loc = set(collect_symbols())
    connected_gears = defaultdict(list)
    part_numbers = []

    with open('input.txt') as fp:
        row = 0
        pns = []
        for line in fp.readlines():
            line = line.rstrip()
            row += 1
            part_numbers += get_part_numbers(row, line)

    for pn in part_numbers:
        gear = set(pn.generate_adjacent()) & gear_loc
        if len(gear) == 1:
            # add part_number to gear
            connected_gears[list(gear)[0]].append(pn)
        elif len(gear) == 2:
            pdb.set_trace()

    # where there are 2 partnumbers on a gear, sum products
    total = 0
    for gear, pn_list in connected_gears.items():
        if len(pn_list) == 2:
            total += pn_list[0].value * pn_list[1].value
    print(total)

                

part2()