
def move(p, c):
    x, y = p
    if c == '|':
        pos1 = x, y-1
        pos2 = x, y+1
        return pos1, pos2
    elif c == '-':
        pos1 = x-1, y
        pos2 = x+1, y
        return pos1, pos2       
    elif c == 'L':
        pos1 = x, y-1
        pos2 = x+1, y
        return pos1, pos2    
    elif c == 'J':
        pos1 = x, y-1
        pos2 = x-1, y
        return pos1, pos2    
    elif c == '7':
        pos1 = x-1, y
        pos2 = x, y+1
        return pos1, pos2    
    elif c == 'F':
        pos1 = x, y+1
        pos2 = x+1, y
        return pos1, pos2    
    else:
        assert 'c' == '.'

def part1():

    m = []
    with open('input.txt') as fp:
        for line in fp.readlines():
            m.append(list(line.rstrip()))
                     
    next_pos = 44, 92
    pos = 43, 92
    i=0
    while next_pos != (43, 92):
        i += 1
        x, y = next_pos
        connections = move(next_pos, m[y][x])
        if connections[0] == pos:
            pos = next_pos
            next_pos = connections[1]
        else:
            pos = next_pos
            next_pos = connections[0]
        print(f'move {i}  pos {pos}  next_pos {next_pos} move {m[y][x]}')
    print((i-1)/2 + 1)

part1()