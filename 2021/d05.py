def sign(x):
    return bool(x > 0) - bool(x < 0)

def srange(start, end):
    # takes ints
    s = sign(end - start)
    return range(start, end + s, s)

def count(l):
    counter = {}
    for x in l:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    return counter

def part1(lines, part2 = False):
    result = []
    for line in lines:
        x, y = zip(*line)
        horz, vert = (x[0] == x[1], y[0] == y[1])
        if horz:
            ys = srange(y[0], y[1])
            xs = len(ys)*[x[0]]
        elif vert:
            xs = srange(x[0], x[1])
            ys = len(xs)*[y[0]]
        else:
            if not part2:
                continue
            xs = srange(x[0], x[1])
            ys = srange(y[0], y[1])
        result.extend(zip(xs, ys))
    counter = count(result)
    return len([k for k, v in counter.items() if v > 1])

def parseinput(fn):
    result = []
    rows = [l.split(' -> ') for l in readlines(fn)]
    for r in rows:
        start, end = r
        result.append([
            [int(x) for x in start.split(',')],
            [int(x) for x in end.split(',')]
        ])
    return result

def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

if __name__ == '__main__':
    fn = 'd05.txt'
    # fn = 'd05eg.txt'
    lines = parseinput(fn)
    print(part1(lines))
    print(part1(lines, part2 = True))
