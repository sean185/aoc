import time
s = time.time()

with open('day1.txt') as f:
    # data = sorted([int(l) for l in f.read().splitlines()]) # faster @ 0.000881s
    data = [int(l) for l in f.read().splitlines()] # slower @ 0.249284s

def part1():
    for x in data:
        for y in data:
            if x+y == 2020:
                print(x,y)
                return x*y

print(part1())

def part2():
    for x in data:
        for y in data:
            for z in data:
                if x+y+z == 2020:
                    print(x,y,z)
                    return x*y*z

print(part2())

print('time taken', time.time()-s, 'secs')