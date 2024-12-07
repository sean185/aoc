from time import time
from pprint import pprint 

def get_neighbours(point, n):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbours = []
    for d in dirs:
        v, h = nb = [x + y for x, y in zip(point, d)]
        if (0 <= v < n) and (0 <= h < n):
            neighbours.append(nb)
    return neighbours

def part1(map):
    start = (0, 0)
    n = len(map) # vertical
    m = len(map[0]) # horizontal
    visited = [[False for _ in range(m)] for _ in range(n)]
    distance = [[float('inf') for _ in range(m)] for _ in range(n)]
    distance[0][0] = 0
    pqueue = [start]
    while len(pqueue) > 0:
        cv, ch = curr = pqueue.pop(0)
        neighbours = [(v, h) for v, h in get_neighbours(curr, n) if visited[v][h] is False]
        for v, h in neighbours:
            new_d = distance[cv][ch] + map[v][h]
            distance[v][h] = min(new_d, distance[v][h]) # check if lower than exisiting distance
        visited[cv][ch] = True
        pqueue.extend(neighbours)
        pqueue = list(set(pqueue))
        pqueue.sort(key=lambda x: distance[x[0]][x[1]])
    return distance[-1][-1]

def part2(map):
    offset = [[i+j for j in range(5)] for i in range(5)]
    result = []
    for i in range(5):
        for v in map:
            row = []
            for j in range(5):
                for h in v:
                    r = h + i + j
                    row.append(r % 9 if r > 9 else r)
            result.append(row)
    return part1(result)

def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

if __name__ == '__main__':
    fn = 'd15.txt'
    # fn = 'd15eg.txt'
    map = [[int(x) for x in l] for l in readlines(fn)]

    start = time()
    print(part1(map))
    print('part1:', time() - start)

    start = time()
    print(part2(map))
    print('part2:', time() - start)
