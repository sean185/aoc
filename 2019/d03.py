def getpath(d):
    path = [(0, 0)] # assume starting point of (0, 0)
    for action in d:
        last = path[-1]
        dir = action[0]
        mag = int(action[1:])
        if dir == 'U':
            walk = [(last[0], last[1]+i+1) for i in range(mag)]
        if dir == 'D':
            walk = [(last[0], last[1]-i-1) for i in range(mag)]
        if dir == 'L':
            walk = [(last[0]-i-1, last[1]) for i in range(mag)]
        if dir == 'R':
            walk = [(last[0]+i+1, last[1]) for i in range(mag)]
        path.extend(walk)
    return path

if __name__ == '__main__':
    with open('day3_input.txt') as f:
        input = f.read().splitlines()
    directions = [x.split(',') for x in input]
    path1, path2 = [getpath(d) for d in directions]
    crosses = set(path1).intersection(set(path2))
    part1 = min([sum(map(abs,c)) for c in crosses if c != (0,0)])
    part2 = min([path1.index(c)+path2.index(c) for c in crosses if c != (0,0)])
    print(part1, part2)