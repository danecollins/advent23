from collections import Counter
import pdb

test = 'Game 1: 14 green, 8 blue, 9 red; 5 blue, 4 green, 2 red; 4 red, 4 blue, 4 green; 1 blue, 3 green, 2 red; 10 red, 3 blue, 15 green; 2 red, 6 green, 3 blue'


def pulls_to_max_balls(input):
    pulls = input.split(';')
    ball_counter_max = Counter()
    for pull in pulls:
         for balls in pull.split(','):
              balls = balls.strip()
              (count, color) = balls.split(' ')
              count = int(count)
              if count > ball_counter_max[color]:
                   ball_counter_max[color] = count
    return ball_counter_max


def part1():
    bag = {'red': 12, 'green': 13, 'blue': 14}
    game_sum = 0

    with open('input.txt') as fp:
        for line in fp.readlines():
            legal = True
            line = line.rstrip()
            (x, y) = line.split(':')
            x = x.replace('Game ', '')
            game_number = int(x)
            ball_count = pulls_to_max_balls(y)
            # test if too many balls
            for color, count in ball_count.items():
                if count > bag[color]:
                    print(f'Game {game_number} has {count} {color} balls')
                    legal = False
                    break
            # all tests passed
            if legal:
                print(f'Game {game_number} passed.')
                game_sum += game_number

        print(f'Part 1 sum of games = {game_sum}')

def part2():
    bag = {}
    game_sum = 0

    with open('input.txt') as fp:
        for line in fp.readlines():
            legal = True
            line = line.rstrip()
            (x, y) = line.split(':')
            x = x.replace('Game ', '')
            game_number = int(x)
            ball_count = pulls_to_max_balls(y)
            p = ball_count['red'] * ball_count['blue'] * ball_count['green']
            game_sum += p
            
        print(f'Part 2 sum of games = {game_sum}')   

part2()