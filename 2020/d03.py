import time
s = time.time()

with open('day3.txt') as f:
    data = f.read().splitlines()

def part1(land, slope):
    x = 0; y = 0; trees = 0
    dx, dy = slope
    while x<len(land):
        trees += data[x][y%len(land[0])] == "#"
        x += dx; y += dy
    return trees

print(part1(data, (1, 3)))

def part2(slopes):
    result = 1
    for slope in slopes:
        result *= part1(data, slope)
    return result

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
print(part2(slopes))

print('time taken', time.time()-s, 'secs')