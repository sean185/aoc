filename = 'd01.txt'

with open(filename) as f:
    txt = f.read().splitlines()

# part 1
L = []
R = []
for line in txt:
    left, right = line.split()
    L.append(int(left))
    R.append(int(right))
L.sort()
R.sort()

total = 0
for l, r in zip(L, R):
    total += abs(l-r)
print(total)

# part 2
total = 0
for l in L:
    total += l * sum([1 for r in R if r == l])
print(total)
