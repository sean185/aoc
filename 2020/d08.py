import time
start = time.time()

with open('day8.txt') as f:
    data = f.read().splitlines()

# part 1
def part1(instructions):
    pos = 0
    acc = 0
    visited = set()
    repeated = False
    while 0 <= pos < len(instructions):
        if pos in visited:
            repeated = True
            break
        visited.add(pos)
        op, n = instructions[pos].split()
        n = int(n)
        if op == 'jmp':
            pos += n
            continue
        if op == 'acc':
            acc += n
        pos += 1
    # print(pos, acc, repeated, visited)
    return acc, repeated

print(part1(data))

# part 2
possibilities = []
for i, d in enumerate(data):
    op, n = d.split()
    if op == 'acc':
        continue
    if op == 'jmp':
        tmp = data.copy()
        tmp[i] = d.replace('jmp','nop')
    if op == 'nop':
        tmp = data.copy()
        tmp[i] = d.replace('nop','jmp')
    possibilities.append(tmp)

print(len(possibilities))
for p in possibilities:
    acc, rpt = part1(p)
    if not rpt:
        print(acc)

print('time taken', time.time()-start, 'secs')