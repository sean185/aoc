fn = 'd06eg.txt'
fn = 'd06.txt'

with open(fn) as f:
    fishes = f.read().splitlines()[0].split(',')
    fishes = list(map(int, fishes))

def sim(fishes, days):
    counter = dict()
    for fish in fishes:
        counter[fish] = counter.get(fish, 0) + 1
    for _ in range(days):
        counter = dict([(x-1, y) for x, y in counter.items()])
        newborn = counter.pop(-1, 0)
        counter[6] = counter.get(6, 0) + newborn
        counter[8] = counter.get(8, 0) + newborn
    return sum(counter.values())

# part 1
print(sim(fishes, 18))
print(sim(fishes, 80))
# part 2
print(sim(fishes, 256))
