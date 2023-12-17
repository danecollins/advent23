    
def approx_match(l1, l2): 
    errors = 0
    for a, b in zip(l1, l2):
        for i in range(len(a)):
            if a[i] != b[i]:
                errors += 1
    return errors == 1

def vert_sym(data):
    max_match = 0
    result = 0
    lines = data
    for i in range(1, len(lines)):
        l1 = list(reversed(lines[:i]))
        l2 = lines[i:]
        shortest = min(len(l1), len(l2))
        l1 = l1[:shortest]
        l2 = l2[:shortest]
        if approx_match(l1, l2):
            # if len(l1) > max_match:
            #     max_match = len(l1)
            result = i
            print(f'Match on index {i}')
    return result

def hor_sym(data):
    print('horizontal check')
    lines = []
    data_len = len(data)
    for i in range(len(data[0])):
        s = ''
        for line in data:
            s += line[i]
        lines.append(s)
    result = vert_sym(lines)
    return result


def part1():

    m = []
    total = 0
    puzzle = 0
    with open('input.txt') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            if line == '':
                print(m)
                puzzle += 1
                v = 100 * vert_sym(m) + hor_sym(m)
                print(f'puzzle {puzzle} - {v}')
                total += v
                m = []
            else:
                m.append(line)
    print(total)


part1()