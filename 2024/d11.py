inp = "125 17"
inp = "77 515 6779622 6 91370 959685 0 9861"
stones = {int(x):1 for x in inp.split()}

def add(d, k, v):
    d[k] = d.get(k, 0) + v

def part1(stones, n):
    oldstones = stones.copy()
    for _ in range(n):
        newstones = {}
        for stone, count in oldstones.items():
            if stone == 0:
                nstone = 1
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                nstone = int(s[:len(s)//2])
                add(newstones, nstone, count) # extra work
                nstone = int(s[len(s)//2:])
            else:
                nstone = stone*2024
            add(newstones, nstone, count)
        oldstones = newstones.copy()
    return sum([v for v in oldstones.values()])

print(part1(stones, 25))
print(part1(stones, 75)) # part 2