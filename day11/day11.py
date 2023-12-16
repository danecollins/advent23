from itertools import combinations


def part1():
    with open('input.txt') as fp:
        lines = [list(x.rstrip()) for x in fp.readlines()]

    expansion_coef = 999999
    total_expansion = 0

    # compute expanded x
    adjusted_x_index = []
    xdim = len(lines[0])
    ydim = len(lines)
    for col in range(xdim):
        chars_in_col = [line[col] for line in lines]
        if all([char == '.' for char in chars_in_col]):
            total_expansion += expansion_coef
        adjusted_x_index.append(col + total_expansion)

    print(adjusted_x_index)

    total_expansion = 0
    adjusted_y_index = []
    for row in range(ydim):
        chars_in_row = lines[row]
        #print(chars_in_row)
        if all([char == '.' for char in chars_in_row]):
            total_expansion += expansion_coef
        adjusted_y_index.append(row + total_expansion)
        
    print(adjusted_y_index)

    galaxies = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                galaxies.append([col, row])
    # print(galaxies)

    total_distance = 0

    for g1, g2 in combinations(galaxies, 2):
        x1 = adjusted_x_index[g1[0]]
        y1 = adjusted_y_index[g1[1]]
        x2 = adjusted_x_index[g2[0]]
        y2 = adjusted_y_index[g2[1]]
        distance = abs(x2 - x1) + abs(y2 - y1)
        # print(f'{g1} - {g2} distance {distance}')
        # print(f'({x1}, {x2}) - ({x2}, {y2}) distance {distance}\n')
        total_distance += distance

    print(total_distance)
part1()


    