import re


def s_to_values(s):
    s = s.strip()
    return [int(x) for x in s.split(' ')]

class MapObject:
    def __init__(self, s):
        (x, y, z) = s_to_values(s)
        self.start = y
        self.end = y + z
        self.offset = x - y

    def mapvalue(self, value):
        if self.start <= value < self.end:
            return value + self.offset
        else:
            return value
    
    def __str__(self):
        return f'S: {self.start}, E: {self.end}, Offset: {self.offset}'
        

def read_map(fp):
    maps = []
    line = fp.readline().rstrip()
    assert 'map' in line
    line = fp.readline().rstrip()
    while line != '':
        print(f'> {line}')
        maps.append(MapObject(line))
        line = fp.readline().rstrip()
    print(maps[0])
    return maps


def read_file():
    with open('input.txt') as fp:
        line = fp.readline().rstrip()
        print(line)
        seeds = s_to_values(line[6:])
        fp.readline()
        map1 = read_map(fp)
        map2 = read_map(fp)
        map3 = read_map(fp)
        map4 = read_map(fp)
        map5 = read_map(fp)
        map6 = read_map(fp)
        map7 = read_map(fp)

    return seeds, [map1, map2, map3, map4, map5, map6, map7]

def part1():
    p = False
    locations = []
    seeds, map_tables = read_file()
    for seed in seeds:
        if seed == 14:
            p = True
        else:
            p = False
        for table in map_tables:
            for map in table:
                newseed = map.mapvalue(seed)
                if seed != newseed:
                    seed = newseed
                    break

        locations.append(seed)
        print(seed)
    
    print(min(locations))

part1()