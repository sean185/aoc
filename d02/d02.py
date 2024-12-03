filename = 'd02eg.txt'
filename = 'd02.txt'
with open(filename) as f:
    txt = f.read().splitlines()

inps = []
for line in txt:
    inps.append([int(x) for x in line.split()])

# part 1
def check(l):
    comb = list(zip(l[:-1], l[1:]))
    fwd = all([1<= (j-i) <= 3 for i, j in comb])
    bwd = all([-3<= (j-i) <= -1 for i, j in comb])
    return fwd or bwd

print(sum([check(l) for l in inps]))

# part 2
total = 0
for l in inps:
    if check(l):
        total += 1
        continue
    for i in range(len(l)):
        if check(l[0:i]+l[i+1:]):
            total += 1
            break
print(total)