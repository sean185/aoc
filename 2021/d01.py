def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

def part1(depths):
    return sum(map(lambda x,y: x<y, depths[:-1], depths[1:]))
    
def part2(depths):
    return part1([x+y+z for x,y,z in zip(depths[:-2], depths[1:-1], depths[2:])])

if __name__ == '__main__':
    fn = 'd01.txt'
    # fn = 'd01eg.txt'
    data = [int(x) for x in readlines(fn)]
    print(part1(data))
    print(part2(data))
