import time
start = time.time()

with open('day7.txt') as f:
    data = f.read().splitlines()

def parse_bags(d):
    parent, children = d.split(' contain ')
    parent = ''.join(parent.split()[:2])
    result = []
    for c in children.split(','):
        if 'no' in c:
            result.append({
                'parent': parent,
                'child': None,
                'weight': None
                })
            continue
        weight, meta, color, _ = c.split()
        result.append({
            'parent': parent,
            'child': meta+color,
            'weight': int(weight)
            })
    return result

edges = []
for d in data:
    edges.extend(parse_bags(d))
# print(edges)

# part 1
path = [['shinygold']]

while True:
    parents = [e['parent'] for e in edges if e['child'] in path[-1]]
    # print(parents)
    path.append(parents)
    if len(parents) == 0:
        break

final = []
for p in path[1:]:
    final.extend(p)
print(len(set(final)))


# part 2

path = [[{'child':'shinygold', 'weight':1}]]
while True:
    all_children = []
    for parent in path[-1]:
        for e in edges:
            if not e['parent'] == parent['child']:
                continue
            # print(e)
            all_children.append({
                'parent': e['parent'],
                'child': e['child'],
                'weight': parent['weight'] * (0 if e['weight'] is None else e['weight'])
            })
        # print(all_children)
    path.append(all_children)
    if len(all_children) == 0:
        break

# from pprint import pprint
# pprint(path)

total = 0 
for p in path[1:-1]:
    total += sum([e['weight'] for e in p])

print(total)

print('time taken', time.time()-start, 'secs')