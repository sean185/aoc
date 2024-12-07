import networkx as nx
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
            result.append([parent, None, None])
            # result.append({
                # 'parent': parent,
                # 'child': None,
                # 'weight': None
                # })
            continue
        weight, meta, color, _ = c.split()
        # result.append({
            # 'parent': parent,
            # 'child': meta+color,
            # 'weight': int(weight)
            # })
        result.append([parent, meta+color, int(weight)])
    return result

edges = []
for d in data:
    edges.extend(parse_bags(d))
# print(edges)

# part 1 - recursion
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

def find_all_parents(node):
    parents = list(G.predecessors(node))
    nodes = parents.copy()
    for p in parents:
        # print(p)
        nodes.extend(find_all_parents(p))
    return nodes

print(len(set(find_all_parents('shinygold'))))

# part 2 - recursion
def find_total_children(node):
    name, qty = node
    children = list(G.successors(name))
    if children == [None]:
        return qty
    # print(node, children)
    tally = qty
    for c in children:
        # print(c, G[name][c])
        tally += find_total_children((c, qty * G[name][c]['weight']))
    return tally

print(find_total_children(('shinygold', 1))-1)

print('time taken', time.time()-start, 'secs')