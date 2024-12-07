fn = 'd14eg.txt'
fn = 'd14.txt'
with open(fn) as f:
    txt = f.read().splitlines()

template = txt[0]
mappings = {x[:2]: (x[0]+x[-1], x[-1]+x[1]) for x in txt[2:]}

initial = list(map(lambda x, y: x + y, template[:-1], template[1:]))

def part1(pairs, n):
    result = pairs
    for i in range(n):
        # print(i)
        after = []
        for p in result:
            after.extend(mappings[p])
        result = after
    polymer = pairs[0][0] + ''.join([x[1] for x in result])
    counter = dict()
    for c in polymer:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    nums = counter.values()
    return max(nums) - min(nums)

print(part1(initial, 10))

def part2():
    pairs = [x[:2] for x in txt[2:]]
    map = [(pairs.index(x[0]+x[-1]), pairs.index(x[-1]+x[1])) for x in txt[2:]]

    start = [0]*len(pairs)
    for p in initial:
        start[pairs.index(p)] += 1

    for _ in range(40):
        before = [0]*len(pairs)
        for i, qty in enumerate(start):
            lhs, rhs = map[i]
            before[lhs] += qty
            before[rhs] += qty
        start = before

    finalcount = dict()
    for p, qty in zip(pairs, start):
        k = p[1]
        if k in finalcount:
            finalcount[k] += qty
        else:
            finalcount[k] = qty
    finalcount[template[0]] += 1

    nums = finalcount.values()
    return max(nums) - min(nums)

print(part2())