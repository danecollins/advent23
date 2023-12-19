import numpy as np
from collections import Counter
import pdb

CAR_LIST = []
VISITED = set()

class Car:
    i = 0
    def __init__(self, x, y, dir):
        global CAR_LIST
        Car.i += 1
        self.id = Car.i
        self.x = x
        self.y = y
        self.dir = dir
        CAR_LIST.append(self)


    def move(self):
        global VISITED
        moves = dict(N=(0, -1), S=(0, 1), E=(1, 0), W=(-1, 0))
        if (self.x, self.y, self.dir) in VISITED:
            self.remove()
            return
        else:
            VISITED.add((self.x, self.y, self.dir))
        
        self.x = self.x + moves[self.dir][0]
        self.y = self.y + moves[self.dir][1]
        if (min(self.x, self.y) < 0) or (self.x > MAX_X) or (self.y > MAX_Y):
            print(f'{self} out of bounds')
            self.remove()
            return

        next_char = LAYOUT[self.y, self.x]

        if next_char == '.':
            return
        elif next_char == '|':
            if (self.dir == 'N') or (self.dir == 'S'):
                return
            elif (self.dir == 'E') or (self.dir == 'W'):
                self.dir = 'N'
                print(f'New car: {Car(self.x, self.y, "S")}')
        elif next_char == '-':
            if (self.dir == 'W') or (self.dir == 'E'):
                return
            elif (self.dir == 'N') or (self.dir == 'S'):
                self.dir = 'E'
                print(f'New car: {Car(self.x, self.y, "W")}')
        elif next_char == '/':
            slash = dict(N = 'E', S = 'W', E = 'N', W = 'S')
            self.dir = slash[self.dir]
        elif next_char == '\\':
            backslash = dict(N = 'W', S = 'E', E = 'S', W = 'N')
            self.dir = backslash[self.dir]


    def remove(self):
        print('in remove')
        print(CAR_LIST)
        for i, c in enumerate(CAR_LIST):
            if self.id == c.id:
                print(f' Removing {self}')
                del CAR_LIST[i]
        print(CAR_LIST)

    def __eq__(self, o):
        return self.id == o.id
    
    def __str__(self):
        return f'car(id={self.id}, {self.x+1}, {self.y+1}, {self.dir})'
    
    def __repr__(self):
        return f'car(id={self.id}, {self.x+1}, {self.y+1}, {self.dir})'

def read_input():

    global LAYOUT, MAX_X, MAX_Y
    with open('input.txt') as fp:
        lines = [line.strip() for line in fp.readlines()]
        num_rows = len(lines)
        MAX_Y = num_rows - 1
        num_cols = len(lines[0])
        MAX_X = num_cols - 1
        print(f'MAX_X = {MAX_X} - MAX_Y = {MAX_Y}')

        LAYOUT = np.empty((num_rows, num_cols), dtype='U1')
        for i, line in enumerate(lines):
            LAYOUT[i, :len(line)] = list(line)

    return LAYOUT

def part1():
    read_input()
    starting_location = Car(0, 0, 'S')
    CAR_LIST.append(starting_location)
    
    while CAR_LIST:
        car = CAR_LIST[0]
        print(f'Move {car}')
        car.move()

    # for i in range(MAX_Y+1):
    #     print("".join(LAYOUT[0:][i]))

    unique_locations = set([(x, y) for (x, y, d) in VISITED])
    print(len(unique_locations))
    for x, y in unique_locations:
        LAYOUT[y][x] = '#'

    for i in range(MAX_Y+1):
        print("".join(LAYOUT[0:][i]))


def part2():
    global VISITED, CAR_LIST
    read_input()
    starting_locations = []
    #for i in range(MAX_X):
        #starting_locations.append((i, 0, 'S'))
        #starting_locations.append((i, MAX_Y, 'N'))
    for i in range(MAX_Y):
    #     starting_locations.append((0, i, 'E'))
        starting_locations.append((MAX_X, i, 'W'))

    max_energized = 0
    for s in starting_locations:
        print(f'starting at {s}')
        VISITED = set()
        CAR_LIST = [Car(s[0], s[1], s[2])]
        while CAR_LIST:
            car = CAR_LIST[0]
            if (car.x < 0) or (car.y < 0):
                pdb.set_trace()
            print(f'Move {car}')
            car.move()

        unique_locations = set([(x, y) for (x, y, _) in VISITED])
        max_energized = max(max_energized, len(unique_locations))
    print(max_energized)


part2()