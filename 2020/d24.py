basis = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (0, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (0, -1),
    }

def parse_bearings(l):
    l = list(l)
    bearings = []
    while len(l) > 0:
        if l[0] in ('s','n'):
            bearings.append(l.pop(0) + l.pop(0))
        else:
            bearings.append(l.pop(0))
    return bearings

def lay_tiles(infile):
    with open(infile) as f:
        instructions = [parse_bearings(x) for x in f.read().splitlines()]
    black_tiles = set()
    for inst in instructions:
        coords = [basis[d] for d in inst]
        tile = (0, 0)
        for coord in coords:
            tile = add(tile, coord)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    return black_tiles

def add(t1, t2):
    return tuple(sum(x) for x in zip(t1,t2))

def get_adj(t):
    return set(add(t, v) for k, v in basis.items())

def part1(infile):
    black_tiles = lay_tiles(infile)
    return len(black_tiles)

def part2(infile, n):
    black_tiles = lay_tiles(infile)
    for _ in range(n):
        # initialize search space
        search_space = set(black_tiles)
        black_to_flip = set()
        white_to_flip = set()
        for tile in black_tiles:
            search_space.update(get_adj(tile))
        for tile in search_space:
            num_black = len(get_adj(tile).intersection(black_tiles))
            if tile in black_tiles:
                if (num_black == 0) or (num_black > 2):
                    black_to_flip.add(tile)
            else:
                if num_black == 2:
                    white_to_flip.add(tile)
        black_tiles.difference_update(black_to_flip)
        black_tiles.update(white_to_flip)
    return len(black_tiles)

infile = 'day24eg.txt'
infile = 'day24.txt'
print('Part 1', part1(infile))
print('Part 2', part2(infile, 100))
