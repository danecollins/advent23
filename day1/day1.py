import re
import pdb


def part1():
    pat1 = re.compile('([0-9]).*')
    pat2 = re.compile('.*([0-9])')

    sum = 0
    with open('input.txt') as fp:
        for line in fp.readlines():
            first = pat1.search(line)
            (i,) = first.groups()
            second = pat2.search(line)
            (j,) = second.groups()
            sum += 10 * int(i) + int(j)

    print(f'The result for part 1 is: {sum}')



def fix(line):
    subst = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    print(line)
    for k, v in subst.items():
        pos = line.find(k)
        while pos >= 0:
            line = line[:pos+1] + v + line[pos+2:]
            pos = line.find(k)
    return line

def part2():
    pat1 = re.compile('([0-9]).*')
    pat2 = re.compile('.*([0-9])')


    sum = 0
    with open('input.txt') as fp:
        for line in fp.readlines():
            line = line.strip()
            line = fix(line)
            first = pat1.search(line)
            (i,) = first.groups()
            second = pat2.search(line)
            (j,) = second.groups()
            sum += 10 * int(i) + int(j)

    print(f'The result for part 2 is: {sum}')


part1()
part2()