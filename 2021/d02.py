def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

def part1(instructions):
    # over thought this, can't apply to part 2
    mapping = {
        'forward': lambda x: (x, 0),
        'up': lambda x: (0, -x),
        'down': lambda x: (0, x)
    }
    displacements = [mapping[inst](mag) for inst, mag in instructions]
    dx, dy = zip(*displacements)
    return sum(dx) * sum(dy)
    
def part2(instructions):
    horz, vert, aim = 0, 0, 0
    for inst, mag in instructions:
        if inst == 'up':
            aim -= mag
        elif inst == 'down':
            aim += mag
        else:
            horz += mag
            vert += mag * aim
    return horz * vert

if __name__ == '__main__':
    fn = 'd02.txt'
    # fn = 'd02eg.txt'
    data = []
    for x in readlines(fn):
        inst, mag = x.split(' ')
        data.append((inst, int(mag)))
    print(part1(data))
    print(part2(data))
