import re

class StepIterator:
    def __init__(self, initial_list):
        self.initial_list = initial_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.initial_list) == 0:
            raise StopIteration

        result = self.initial_list[self.index]
        self.index = (self.index + 1) % len(self.initial_list)
        return result


def read_input():
    mymap = dict()
    pat = re.compile(r'([\w]+) = \(([\w]+), ([\w]+)\)')

    with open('input.txt') as fp:
        line = fp.readline()
        step = StepIterator(list(line.rstrip()))
        _ = fp.readline()
        line = fp.readline().rstrip()
        while line:
            # NQT = (TXC, RVJ)  
            f, l, r = pat.search(line).groups()
            mymap[f] = dict(L=l, R=r)
            line = fp.readline().rstrip()

    return step, mymap

def part1():
    step, mymap = read_input()
    step_to_take = next(step)
    current_location = 'AAA'
    step_number = 1
    while current_location != 'ZZZ':
        print(f'{step_number} step {step_to_take} from {current_location} to ', end='')
        current_location = mymap[current_location][step_to_take]
        print(f'{current_location}')
        step_number += 1
        step_to_take = next(step)

    print(f'Took {step_number-1} steps')

def part2():
    step, mymap = read_input()

    current_locations = [L for L in mymap.keys() if L[2] == 'A']
    z_locations = []
    step_to_take = next(step)
    step_number = 1
    print(f'current_location: {[X[2] for X in current_locations]}')
    while len(z_locations) != len(current_locations):
        current_locations = [mymap[CL][step_to_take] for CL in current_locations]
        z_locations = [L for L in current_locations if L[2] == 'Z']
        if len(z_locations) > 1:
            print(f'{step_number} - {z_locations}')
        step_number += 1
        step_to_take = next(step)

    print(f'Took {step_number-1} steps')



part2()