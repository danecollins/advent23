import re
from collections import OrderedDict, defaultdict
import pdb

def read_file():
    with open('input.txt') as fp:
        lines = fp.readlines()
        lines = [line.rstrip() for line in lines]
    return "".join(lines)

def hash_inst(s):
    ascii_list = [ord(x) for x in list(s)]
    code = 0
    for a in ascii_list:
        code += a
        code *= 17
        code = code % 256
    return code

def part1():
    instructions = read_file().split(',')
    hashes = [hash_inst(x) for x in instructions]
    for x in instructions:
        print(x, hash_inst(x))

    print(sum(hashes))


def part2():
    instructions = read_file().split(',')
    pat1 = re.compile(r'(\w+)-')
    pat2 = re.compile(r'(\w+)=(\d+)')
    boxes = defaultdict(OrderedDict)
    for inst in instructions:
        g = pat1.match(inst)
        if g:
            # remove
            label = g.groups()[0]
            box_number = hash_inst(label)
            box = boxes[box_number]
            if label in box:
                del box[label]
            print(f"removed '{label}' from box {box_number}")

        else:
            g = pat2.match(inst)
            if not g:
                pdb.set_trace()
            (label, power) = g.groups()
            label = g.groups()[0]
            box_number = hash_inst(label)
            box = boxes[box_number]
            box[label] = int(power)
            print(f'set {label}={power} in box {box_number}')
    
    total = 0
    for box_number in range(256):
        if box_number in boxes:
            box_total = 0
            box = boxes[box_number]
            for slot, power in enumerate(box.values(), 1):
                box_total += (box_number + 1) * slot * power
            print(f'{box_number} = {box}   {box_total}')
            total += box_total
    print(total)

part2()