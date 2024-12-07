def part1(crabs):
    m = max(crabs)
    spaces = list(range(m+1))
    for i in range(m+1):
        spaces[i] = sum([abs(i-c) for c in crabs])
    return min(spaces)

def part2():
    pass

def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

if __name__ == '__main__':
    fn = 'd07.txt'
    fn = 'd07eg.txt'
    crabs = [int(x) for x in readlines(fn)[0].split(',')]
    print(part1(crabs))
