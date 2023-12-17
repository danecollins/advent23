
def sort_string(s):
    return ''.join(sorted(s, reverse=True))

def part1():
    with open('input.txt') as fp:
        lines = fp.readlines()
        lines = [line.strip() for line in lines]

# Transpose the lines to create 10 strings with data in each column
    columns = []
    for i in range(len(lines[0])):
        columns.append(''.join([row[i] for row in lines]))

    pushed = []
    for col in columns:
        new_col = "#".join([sort_string(x) for x in col.split('#')])
        pushed.append(new_col)

    # compute load
    total = 0
    for i, row_from_bottom in enumerate(range(len(pushed[0]), 0, -1)):
        rocks = sum([1 for c in pushed if c[i] == 'O'])
        print(f'row {row_from_bottom} has {rocks} rocks')
        total += row_from_bottom * rocks

    print(total)

                   

part1()