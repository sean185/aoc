def isincreasing(x):
    return str(x) == ''.join(sorted(str(x)))

def hasdupes(x):
    return len(set(str(x))) < len(str(x))

def hasdupes(x):
    return len(set(str(x))) < len(str(x))

def haspair(x):
    d = [str(x).count(i) for i in set(str(x))]
    return 2 in d

if __name__ == '__main__':
    input = '134564-585159'
    start, end = map(int,input.split('-'))
    numrange = list(range(start, end+1))
    numrange = [x for x in numrange if isincreasing(x)]
    numrange = [x for x in numrange if hasdupes(x)]
    part1 = len(numrange)
    numrange = [x for x in numrange if haspair(x)]
    part2 = len(numrange)
    print(part1, part2)
