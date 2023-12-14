import pytest

from day7 import Card, Card2, hand_type

def test_card():
    s = 'J3T3T 868'
    c1 = Card(s)
    assert c1.bet == 868
    assert c1.cards == 'J3T3T'
    assert c1.sortkey == 'B3A3A'
    assert c1.hand_type == hand_type['2pair']

    s = '6Q499 630'
    c2 = Card(s)
    assert c2.sortkey == '6C499'
    assert c2.hand_type == hand_type['pair']

    s = 'JJAAA 335'
    c3 = Card(s)
    assert c3.hand_type == hand_type['fullhouse']
    assert c3.sortkey == 'BBEEE'

    s = 'JJJAA 1'
    c4 = Card(s)
    assert c4 < c3

    assert c2 < c4

    l = sorted([c1, c2, c3, c4])
    assert l[0] == c2
    assert l[1] == c1
    assert l[2] == c4
    assert l[3] == c3

def test_card2():
    s = 'J3T3T 868'
    c1 = Card2(s)
    assert c1.bet == 868
    assert c1.cards == 'J3T3T'
    assert c1.sortkey == 'B3A3A'
    assert c1.hand_type == hand_type['fullhouse']

    hand_type_tests = [('JJJQQ 1', 'five'), ('JJQQQ 1', 'five'), ('J22QQ 1', 'fullhouse'), 
                       ('JJ2QQ 1', 'four'), ('J23QQ 1', 'three'), ('JJ123 1', 'three'),
                       ('22J72 1', 'four'), ('21JJJ 1', 'four')]
    for tst, result in hand_type_tests:
        c = Card2(tst)
        assert c.hand_type == hand_type[result]
