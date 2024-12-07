import time
stopwatch = time.time()

# with open('day14eg.txt') as f:
with open('day14.txt') as f:
    data = f.read().splitlines()

# part 1
def mask1(m, s):
    return ''.join(a if a in list('01') else b for a, b in zip(m, s))

def part1(data):
    result = {}
    for d in data:
        inst, v = d.split(' = ')
        if inst == 'mask':
            m = v
            continue
        address = int(inst.split('[')[-1][:-1])
        new_v = mask1(m, f'{int(v):b}'.zfill(36))
        result[address] = int(new_v, 2)
    return result
        
print(sum(part1(data).values()))
print(time.time() - stopwatch)
stopwatch = time.time()

# part 2
def mask2(m, s):
    rs = [tuple()] # initialize
    for a, b in zip(m, s):
        if a == 'X':
            rs = [r + ('0',) for r in rs] + [r + ('1',) for r in rs]
        if a == '0':
            rs = [r + (b,) for r in rs]
        if a == '1':
            rs = [r + (a,) for r in rs]
    return [''.join(r) for r in rs]

# with open('day14eg2.txt') as f:
with open('day14.txt') as f:
    data = f.read().splitlines()

def part2(data):
    result = {}
    for d in data:
        inst, v = d.split(' = ')
        if inst == 'mask':
            m = v
            continue
        address = int(inst.split('[')[-1][:-1])
        addresses = mask2(m, f'{int(address):b}'.zfill(36))
        for a in addresses:
            result[a] = int(v)
    return result

print(sum(part2(data).values()))
print(time.time() - stopwatch)
