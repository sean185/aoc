from pprint import pprint 

def rinter(r1, r2):
    # any 2 ranges intersect at exactly 2 points
    # rinter((-20,26),(-20,33))
    r1 = sorted(r1)
    r2 = sorted(r2)
    if r1[1] < r2[0] or r1[0] > r2[1]:
        return None
    return (max(r1[0], r2[0]), min(r1[1], r2[1]))

def cinter(c1, c2):
    # any 2 cubes intersect at exactly 8 points
    # cinter(((-20, 26), (-36, 17), (-47, 7)), ((-20, 33), (-21, 23),(-26, 28)))
    inters = []
    for d in zip(c1, c2):
        inters.append(rinter(d[0], d[1]))
    if any([d is None for d in inters]):
        return None
    return inters
    
def parseline(l):
    state, l = l.split(' ')
    dims = []
    for d in l.split(','):
        d = [int(dd) for dd in d[2:].split('..')]
        dims.append(tuple(sorted(d)))
    return (state, tuple(dims))

def count(cuboid):
    # count(((-20, 26), (-36, 17), (-47, 7)))
    volume = 1
    for d in cuboid:
        volume *= d[1]-d[0]+1
    return volume

fn = 'd22eg.txt'
fn = 'd22eg2.txt'
fn = 'd22.txt'
with open(fn) as f:
    txt = f.read().splitlines()

inputs = [parseline(l) for l in txt]

def part2(inputs):
    sofar = []
    for inp in inputs:
        inst, cuboid = inp
        if inst == 'on':
            overlaps = []
            for state, other in sofar:
                inter = cinter(cuboid, other)
                if inter is None:
                    continue
                overlaps.append(('off' if state == 'on' else 'on', inter))
            sofar.append(inp)
            sofar.extend(overlaps)
        if inst == 'off':
            overlaps = []
            for state, other in sofar:
                inter = cinter(cuboid, other)
                if inter is None:
                    continue
                overlaps.append(('off' if state == 'on' else 'on', inter))
            sofar.extend(overlaps)
        print(len(sofar))
    return sum([(1 if s == 'on' else -1)*count(c) for s, c in sofar])

print(part2(inputs[:20]))
print(part2(inputs)) # in the end keeps track of 43656 cuboids



