fn = 'd10eg.txt'
fn = 'd10.txt'
opening = '([{<'
closing = ')]}>'
mapping = dict(zip(opening, closing))

with open(fn) as f:
    txt = f.read().splitlines()

# part 1 - 399153
def part1(line):
    i = 0
    rem = ''
    while i<len(line):
        c = line[i]
        if c in opening:
            rem += c
        elif c == mapping[rem[-1]]:
            # check if it is a corresponding closing brace
            rem = rem[:-1]
        else:
            return c
        i += 1
    return rem

## part 1 v2 - 2995077699
pairs = [''.join(x) for x in zip(opening, closing)]
def part1v2(line):
    while any([p in line for p in pairs]):
        for p in pairs:
            line = line.replace(p, '')
    corrupter = ''
    for c in line:
        if c in closing:
            corrupter = c
            break
    return line if corrupter == '' else corrupter 

checked = [part1(line) for line in txt]
points = dict(zip(closing, (3, 57, 1197, 25137)))
print(sum([points[x] for x in checked if len(x) == 1]))

# part 2
points2 = dict(zip(opening, (1, 2, 3, 4)))
def part2(line):
    total = 0
    for c in reversed(line):
        total = total * 5 + points2[c]
    return total

scores = sorted([part2(x) for x in checked if len(x) != 1])
print(scores[int(len(scores)/2)])


import time
def bench_part1():
    [part1(line) for line in txt]

def bench_part1v2():
    [part1v2(line) for line in txt]

import timeit
num_runs = 1000
duration = timeit.Timer(bench_part1).timeit(number = num_runs)
avg_duration = duration/num_runs
print(f'On average it took {avg_duration} seconds')

duration = timeit.Timer(bench_part1v2).timeit(number = num_runs)
avg_duration = duration/num_runs
print(f'On average it took {avg_duration} seconds')