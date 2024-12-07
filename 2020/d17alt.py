import timeit

# part 1 
def parser(txt):
    actives = set()
    for y in range(len(txt)):
        for x in range(len(txt[0])):
            if txt[y][x] == '#':
                actives.add((x,y,0)) # z = 0
    return actives

def cross_tuples(a, b):
    result = []
    for x in a:
        for y in b:
            result.append(x + y)
    return result

def getadj(t):
    result = [(t[0]+i,) for i in (-1, 0, 1)]
    for dim in t[1:]:
        result = cross_tuples(result, [(dim+i,) for i in (-1, 0, 1)])
    result.remove(t)
    return set(result)

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
    return len(result)

# part 2 
def parser2(txt):
    actives = set()
    for y in range(len(txt)):
        for x in range(len(txt[0])):
            if txt[y][x] == '#':
                actives.add((x, y, 0, 0)) # z = 0, w = 0
    return actives

def part2(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    
    result = parser2(txt)
    for i in range(6):
        result = iter(result)
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

