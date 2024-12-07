import time
start = time.time()

with open('day6.txt') as f:
    data = f.read().split('\n\n')

def part1(d):
    return len(set(d.replace('\n','')).intersection(set('abcdefghijklmnopqrstuvwxyz')))

print(sum([part1(d) for d in data]))

def part2(d):
    res = d.splitlines()
    init = set(res[0])
    for r in res[1:]:
        r = set(r).intersection(set('abcdefghijklmnopqrstuvwxyz'))
        init = init.intersection(r)
    return len(init)

print(sum([part2(d) for d in data]))

print('time taken', time.time()-start, 'secs')