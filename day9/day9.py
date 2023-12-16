import pdb

def part1():
    sum_of_predictions = 0

    with open('input.txt') as fp:
        for lineno, line in enumerate(fp.readlines(), 1):
            values = [int(x) for x in line.strip().split(' ')]
            sum_last = 0
            last_result = values[-1]
            prediction = 0
            iterations = 0
            print(last_result)
            while any([v != 0 for v in values]):
                iterations += 1
                values = [values[i+1] - values[i] for i in range(len(values) - 1)]
                sum_last += values[-1]
            prediction += (sum_last + last_result)
            #print(prediction)
            #print(f'Line: {lineno}\titerations: {iterations}\tprediction: {prediction}')
            sum_of_predictions += prediction
    print(sum_of_predictions)


def part2():
    sum_of_predictions = 0

    with open('input.txt') as fp:
        for lineno, line in enumerate(fp.readlines(), 1):
            values = [int(x) for x in line.strip().split(' ')]
            values = list(reversed(values))
            sum_last = 0
            last_result = values[-1]
            prediction = 0
            iterations = 0
            while any([v != 0 for v in values]):
                iterations += 1
                values = [values[i+1] - values[i] for i in range(len(values) - 1)]
                sum_last += values[-1]
            prediction += (last_result + sum_last)
            #print(prediction)
            #print(f'Line: {lineno}\titerations: {iterations}\tprediction: {prediction}')
            sum_of_predictions += prediction
    print(sum_of_predictions)


part2()