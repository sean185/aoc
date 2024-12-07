import time
checkpoint = time.time()

with open('day9.txt') as f:
    data = [int(l) for l in f.read().splitlines()]

# part 1
def find_pair(preamble, target):
    for x in preamble:
        for y in preamble:
            if x+y == target:
                return x+y
    return None

preamble_length = 25
for i, pos in enumerate(range(preamble_length, len(data))):
    preamble = data[i:pos]
    target = data[pos]
    pair = find_pair(preamble, target)
    if pair is None:
        print(target)
        break

print(time.time()-checkpoint)
checkpoint = time.time()

# part 2 - this is now in `target` variable
subset = [x for x in data if x < target] # premature optimization

# dict version, needs a helper
def part2(p1, p2):
    return {
        'left': p1.get('left', p1['self']), 
        'self': p1['self']+p2['right'], 
        'right': p2['right']
        }

tmp = [{'left': p1, 'self': p1+p2, 'right': p2} for p1, p2 in zip(subset[:-1], subset[1:])]
for n in range(len(subset)-1): # iterate n-1 times at worst
    tmp = [part2(left, right) for left, right in zip(tmp[:-1], tmp[1:])]
    search = [x for x in tmp if x['self'] == target]
    if len(search) > 0:
        result = search[0]
        final = subset[subset.index(result['left']):subset.index(result['right'])]
        print(min(final) + max(final))
        break

print(time.time()-checkpoint)
checkpoint = time.time()

# tuple version - neater but more confusing?
tmp = [(l, l+r, r) for l, r in zip(subset[:-1], subset[1:])] # initialize
for n in range(len(subset)-1): # iterate n-1 times at worst
    tmp = [(l[0], l[1]+r[2], r[2]) for l, r in zip(tmp[:-1], tmp[1:])]
    search = [x for x in tmp if x[1] == target]
    if len(search) > 0:
        result = search[0]
        final = subset[subset.index(result[0]):subset.index(result[2])]
        print(min(final) + max(final))
        break

print(time.time()-checkpoint)
checkpoint = time.time()

# brute search actually not bad eh
for con in range(2, len(subset)):
    results = [subset[i:i+con] for i in range(len(subset)-con+1) if sum(subset[i:i+con]) == target]
    if len(results) > 0:
        print(min(results[0])+max(results[0]))
        break

print(time.time()-checkpoint)
checkpoint = time.time()
