fn = 'd12eg.txt'
fn = 'd12eg2.txt'
fn = 'd12eg3.txt'
fn = 'd12.txt'

from pprint import pprint

with open(fn) as f:
    edges = [x.split('-') for x in f.read().splitlines()]

links = {}
for e in edges:
    x, y = e
    if x in links:
        links[x].add(y)
    else:
        links[x] = {y}
    if y in links:
        links[y].add(x)
    else:
        links[y] = {x}
links = {k:v - {'start'} for k, v in links.items() if k != 'end'}

# part 1
paths = [['start']]
while not all([x[-1] == 'end' for x in paths]):
    newpaths = []
    for path in paths:
        lastnode = path[-1]
        if lastnode == 'end':
            # nothing further to expand
            newpaths.append(path)
            continue
        for nextnode in links[lastnode]:
            if nextnode.isupper() or nextnode == 'end' or nextnode not in path:
                newpaths.append(path + [nextnode])
    paths = newpaths

print(len(paths))

# part 2
def extra1small(path):
    # returns if there is at most 1 extra small node in the path
    counter = dict()
    for p in path:
        counter[p] = counter.get(p, 0) + 1
    return any([1 < x for x in {k: v for k, v in counter.items() if k.islower()}.values()])

paths = [['start']]
while not all([x[-1] == 'end' for x in paths]):
    newpaths = []
    for path in paths:
        lastnode = path[-1]
        if lastnode == 'end':
            # nothing further to expand
            newpaths.append(path)
            continue
        for nextnode in links[lastnode]:
            if nextnode.isupper() or nextnode == 'end' or nextnode not in path or not extra1small(path):
                newpaths.append(path + [nextnode])
    paths = newpaths

# pprint(paths)
print(len(paths))