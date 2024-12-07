def part1():
    pass

def part2():
    pass

def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

if __name__ == '__main__':
    fn = 'd13.txt'
    fn = 'd13eg.txt'
    print(part1())
