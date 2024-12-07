# with open('day12eg.txt') as f:
with open('day12.txt') as f:
    data = [(l[0], int(l[1:])) for l in f.read().splitlines()]

# part 1
def add(p, d):
    return tuple(x+y for x,y in zip(p, d))

def mult(d, m):
    return tuple(m*i for i in d)

def rot(b, d, m):
    m = m//90
    d = 1 if d == 'R' else -1
    r = m * d + 'NESW'.index(b)
    return 'NESW'[r%4]

basis = {
    'N':(0, 1),
    'E':(1, 0),
    'S':(0, -1),
    'W':(-1, 0)
    }

def part1():
    position = (0, 0)
    bearing = 'E'
    for d in data:
        inst, mag = d
        if inst in list('NESW'):
            displacement = mult(basis[inst], mag)
            position = add(position, displacement)
        if inst in list('LR'):
            bearing = rot(bearing, inst, mag)
        if inst == 'F':
            displacement = mult(basis[bearing], mag)
            position = add(position, displacement)
    return position

def manhattan(t):
    return sum(abs(x) for x in t)

print(manhattan(part1()))

# part 2

def rotcw(w):
    return (w[1], -w[0])

def rotccw(w):
    return (-w[1], w[0])

def rotw(w, d, m):
    r = rotcw if d == 'R' else rotccw
    for i in range(m//90):
        w = r(w)
    return w

def part2():
    position = (0, 0)
    waypoint = (10, 1)
    for d in data:
        inst, mag = d
        if inst in list('NESW'):
            displacement = mult(basis[inst], mag)
            waypoint = add(waypoint, displacement)
        if inst in list('LR'):
            waypoint = rotw(waypoint, inst, mag)
        if inst == 'F':
            displacement = mult(waypoint, mag)
            position = add(position, displacement)
    return position

print(manhattan(part2()))
