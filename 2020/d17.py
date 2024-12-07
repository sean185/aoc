import timeit

##########
# part 1 #
##########

def parser(txt):
    actives = set()
    for y in range(len(txt)):
        for x in range(len(txt[0])):
            if txt[y][x] == '#':
                actives.add((x,y,0)) # z = 0
    return actives

def getadj(t):
    x, y, z = t
    result = []
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == dy == dz == 0:
                    continue
                result.append((x + dx, y + dy, z + dz))
    return set(result)

def printer(result):
    xs, ys, zs = zip(*result)
    minx = min(xs)
    miny = min(ys)
    minz = min(zs)
    maxx = max(xs)
    maxy = max(ys)
    maxz = max(zs)
    # print(minx, maxx)
    # print(miny, maxy)
    # print(minz, maxz)
    for z in range(minz, maxz+1):
        for y in range(miny, maxy+1):
            print(''.join(['#' if (x,y,z) in result else '.' for x in range(minx, maxx+1)]))
        print()

def iter(actives):
    search_space = set()
    for a in actives:
        search_space.update(getadj(a))

    result = set()
    for s in search_space:
        m = len(getadj(s).intersection(actives))
        if s in actives:
            if m in (2, 3):
                result.add(s)
        else:
            if m == 3:
                result.add(s)
    return result

def part1(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    
    result = parser(txt)
    for i in range(6):
        result = iter(result)
        # print(len(result))
        # printer(result)
    return len(result)

##########
# part 2 #
##########

def parser2(txt):
    actives = set()
    for y in range(len(txt)):
        for x in range(len(txt[0])):
            if txt[y][x] == '#':
                actives.add((x, y, 0, 0)) # z = 0, w = 0
    return actives

def getadj2(t):
    x, y, z, w = t
    result = []
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    result.append((x + dx, y + dy, z + dz, w + dw))
    return set(result)

def iter2(actives):
    search_space = set()
    for a in actives:
        search_space.update(getadj2(a))

    result = set()
    for s in search_space:
        m = len(getadj2(s).intersection(actives))
        if s in actives:
            if m in (2, 3):
                result.add(s)
        else:
            if m == 3:
                result.add(s)
    return result

def part2(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    
    result = parser2(txt)
    for i in range(6):
        result = iter2(result)
        # print(len(result))
        # printer(result)
    return len(result)

if __name__ == '__main__':
    # part 1
    start_time = timeit.default_timer()
    print(part1('day17eg.txt'))
    print('Time taken:', timeit.default_timer() - start_time)
    
    start_time = timeit.default_timer()
    print(part1('day17.txt'))
    print('Time taken:', timeit.default_timer() - start_time)

    # part 2
    start_time = timeit.default_timer()
    print(part2('day17eg.txt'))
    print('Time taken:', timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print(part2('day17.txt'))
    print('Time taken:', timeit.default_timer() - start_time)

