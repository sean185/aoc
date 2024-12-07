import time
s = time.time()

with open('day2.txt') as f:
    data = f.read().splitlines()

def part1(l):
    pos, char, string = l.split(' ')
    range = [int(x) for x in pos.split('-')]
    bools = [x == char[0] for x in string]
    return range[0] <= sum(bools) <= range[1]

print(sum([part1(l) for l in data]))

def part2(l):
    pos, char, string = l.split(' ')
    positions = [int(x) for x in pos.split('-')]
    bools = [string[x-1] == char[0] for x in positions]
    return 1 == sum(bools)

print(sum([part2(l) for l in data]))

print('time taken', time.time()-s, 'secs')