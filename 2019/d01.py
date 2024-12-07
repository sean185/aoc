def fold(m):
    r = int(m/3-2)
    if r > 0:
        return r+fold(r)
    return 0

if __name__ == '__main__':
    with open('day1_input.txt') as f:
        input = f.read().splitlines()
    modules = list(map(int, input))
    part1 = sum([int(m/3-2) for m in modules])
    part2 = sum([fold(m) for m in modules])
    print(part1, part2)