import pytest

from day3 import PartNumber, collect_symbols, get_part_numbers


def test_init():
    num = PartNumber(232, 4, 2)

    assert num.value == 232
    assert num.start_col == 4
    assert num.len == 3
    assert num.row == 2

def test_gen_adj():
    num = PartNumber(232, 4, 2)
    adj = num.generate_adjacent()
    assert len(adj) == 15
    assert (1, 3) in adj
    assert (1, 7) in adj
    assert (3,3) in adj
    assert (3,7) in adj
    assert (2, 2) not in adj
    assert (2, 8) not in adj

def test_collect_sym():
    loc = collect_symbols('testinput.txt')
    assert len(loc) == 6
    assert (2, 4) in loc
    assert (5, 4) in loc

def test_get_part_numbers():
    s = '.......87...622.....87.....822.......215..........810'
    pns = get_part_numbers(1, s)
    l = [(p.value, p.start_col) for p in pns]
    assert (87, 8) in l
    assert (87,21) in l
    assert (810, 51) in l
    assert (622, 13) in l
    assert (215, 38) in l
    assert (822, 28) in l
    assert len(l) == 6

    s = r'........@.185........88.........483...208......-..........419..331......460.../46.406.......................582.-....*..........408.........'
    pns = get_part_numbers(1, s)
    l = [(p.value, p.start_col) for p in pns]
    assert len(l) == 11
    assert (185, 11) in l
    assert (88, 22) in l
    assert (483, 33) in l
    assert (208, 39) in l
    assert (419, 59) in l
    assert (331, 64) in l
    assert (460, 73) in l
    assert (46, 80) in l
    assert (406, 83) in l
    assert (582, 109) in l
    assert (408, 129) in l
