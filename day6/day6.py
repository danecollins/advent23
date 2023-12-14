import cmath

#Time:        38     67     76     73
#Distance:   234   1027   1157   1236
races = [(38, 234), (67, 1027), (76, 1157), (73, 1236)]
#Time:      7  15   30
#Distance:  9  40  200
races = [(38677673, 234102711571236)]

def solve_quadratic(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Returns the roots as a tuple.
    """
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two solutions
    root1 = (-b - discriminant) / (2 * a)
    root2 = (-b + discriminant) / (2 * a)

    return root1, root2

def part1():
    option_list = 1
    # speed^2 - total * speed + distance = 0
    for race in races:
        total, distance = race
        lower, upper = solve_quadratic(1, -1 * total, distance + 1)
        print(lower, upper)
        lower = int(abs(lower) + .99)
        upper = int(abs(upper))
        options = upper - lower + 1
        option_list *= options
    
    print(option_list)


part1()
