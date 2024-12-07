from pprint import pprint
import timeit

directions = ('top','right','bottom','left')

def bools_to_int(l):
    return int(''.join('1' if x == '#' else '0' for x in l), 2)

def reverse_hash(edge):
    s = bin(edge)[2:].zfill(10)
    return int(s[::-1], 2)

class Tile():
    def __init__(self, txt):
        parts = txt.splitlines()
        self.id = parts[0].split()[1][:-1]
        self.image = [list(p) for p in parts[1:]]
        self.top_edge = bools_to_int(self.image[0])
        self.right_edge = bools_to_int([i[-1] for i in self.image])
        self.bottom_edge = bools_to_int(self.image[-1])
        self.left_edge = bools_to_int([i[0] for i in self.image])
        self.flipped = False
        self.rot_offset = 0
        self.is_solved = False
        # linked list bit, keeps tileid
        self.top_link = None
        self.right_link = None
        self.bottom_link = None
        self.left_link = None
        
    def rotate(self):
        # always clockwise 90 deg
        # need to shift everything that has a facing
        self.image = [tuple(r[::-1]) for r in zip(*self.image)]
        
    def flip(self, axis):
        # horizontal or vertical
        if axis == 'hori':
            self.image = self.image[::-1]
        elif axis == 'vert':
            self.image = [r[::-1] for r in self.image]

    def get_edge(self, d):
        if d == 'top':
            return bools_to_int(self.image[0])
        elif d == 'right':
            return bools_to_int([i[-1] for i in self.image])
        elif d == 'bottom':
            return bools_to_int(self.image[-1])
        elif d == 'left':
            return bools_to_int([i[0] for i in self.image])
        else:
            pass

    def set_link(self, d, v):
        setattr(self, d+'_link', v)
        
    def get_link(self, d):
        getattr(self, d+'_link')

    def get_all_links(self):
        return {d: getattr(self, d+'_link') for d in directions}
            

    def get_image(self):
        return '\n'.join([''.join(r) for r in self.image])

    def get_all_possible_edges(self):
        edges = [self.get_edge(d) for d in directions]
        mirrored_edges = [reverse_hash(x) for x in edges]
        return edges + mirrored_edges

def parse_tiles(infile):
    with open(infile) as f:
        data = f.read().split('\n\n')
    return [Tile(x) for x in data]

infile = 'day20eg.txt'
infile = 'day20.txt'
Tiles = parse_tiles(infile)

dmap = {
    'top': ('bottom', 'vert'),
    'bottom': ('top','vert'),
    'left': ('right', 'hori'),
    'right': ('left', 'hori')
}

# recursive solver
def solve2(Tiles, tile):
    # try to match every edge
    for d in directions:
        if tile.get_link(d):
            # skip this direction if we're done
            continue
        matched_tile = None
        for t in Tiles:
            if t.id == tile.id:
                continue
            if tile.get_edge(d) in t.get_all_possible_edges():
                matched_tile = t
        if matched_tile is None:
            # skip since this is an edge or corner
            continue
        # assume we've found the one single matching tile
        # and it is already been solved before
        dd, f = dmap[d]
        if matched_tile.is_solved:
            tile.set_link(d, matched_tile)
            matched_tile.set_link(dd, tile)
            continue
        
        for _ in range(4):
            if tile.get_edge(d) == matched_tile.get_edge(dd):
                tile.set_link(d, matched_tile)
                matched_tile.set_link(dd, tile)
                # print(tile.id, d, 'matched', t.id, dd)
                tile.is_solved = True
                break
            elif tile.get_edge(d) == reverse_hash(matched_tile.get_edge(dd)):
                tile.set_link(d, matched_tile)
                matched_tile.set_link(dd, tile)
                matched_tile.flip(f)
                tile.is_solved = True
                break
            if not matched_tile.is_solved:
                matched_tile.rotate()
        if not matched_tile.is_solved:
            solve2(Tiles, matched_tile)
        print(tile.id, d, matched_tile.id)

solve2(Tiles, Tiles[0])

# find top left corner
def find_corners(tiles):
    corners = []
    t = tiles[0]
    while t.top_link is not None:
        t = t.top_link
        print(t.id)
    corners.append(t.id)
    while t.right_link is not None:
        t = t.right_link
        print(t.id)
    corners.append(t.id)
    while t.bottom_link is not None:
        t = t.bottom_link
        print(t.id)
    corners.append(t.id)
    while t.left_link is not None:
        t = t.left_link
        print(t.id)
    corners.append(t.id)
    return corners

# find_corners(Tiles)

t = Tiles[0]
print(t.id)
while t.top_link is not None:
    t = t.top_link
while t.left_link is not None:
    t = t.left_link
print(t.id)
downwards = [t]
grid_size = int(len(Tiles)**0.5)
for _ in range(grid_size-1):
    t = t.bottom_link
    downwards.append(t)

final_image = []
for d in downwards:
    row = [tuple(x[1:-1]) for x in d.image[1:-1]]
    for _ in range(grid_size-1):
        d = d.right_link
        print(d.id)
        tmp = [tuple(x[1:-1]) for x in d.image[1:-1]]
        # pprint(row)
        # pprint(tmp)
        row = [x + y for x, y in zip(row, tmp)]
    final_image.extend(row)

print('\n'.join([''.join(r) for r in final_image]))

ness = [
 '                  # ',
 '#    ##    ##    ###',
 ' #  #  #  #  #  #   '
 ]

def find_nessie(arr):
    nessie = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
    res = all('#' == arr[i][j] for i, j in nessie)
    return res

find_nessie(ness)

def part2(image):
    for _ in range(4):
        found = 0
        for i in range(len(image)-2):
            for j in range(len(image[0])-19):
                found += find_nessie([r[j:j+21] for r in image[i:i+3]])
        # rotate
        image = [r[::-1] for r in zip(*image)] 
        if found > 0:
            return found
    image = image[::-1]
    for _ in range(4):
        found = 0
        for i in range(len(image)-2):
            for j in range(len(image[0])-19):
                found += find_nessie([r[j:j+21] for r in image[i:i+3]])
        # rotate
        image = [r[::-1] for r in zip(*image)] 
        if found > 0:
            return found

print(sum(sum('#' == x for x in r) for r in final_image) - 15*part2(final_image))