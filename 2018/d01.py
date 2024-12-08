filename = "d01.txt"
with open(filename) as f:
    txt = f.read().splitlines()
# part 1
p1 = [int(x) for x in txt]
print(sum(p1))

# part 2
visited = set()
i = 0
curr = 0
while not curr in visited:
    visited.add(curr)
    curr += p1[i % len(p1)]
    i += 1
print(curr)