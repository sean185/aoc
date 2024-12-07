def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

def avg(l):
    return sum(l)/len(l)

def lean(l):
    return 0 < sum([2*x-1 for x in l])

def part1(data):
    d = [avg(x) for x in zip(*data)]
    gamma = int("".join(["0" if x < 0.5 else "1" for x in d]),2)
    epsilon = int("".join(["0" if x > 0.5 else "1" for x in d]),2)
    return gamma * epsilon

def part2(data):
    o2 = data.copy()
    co2 = data.copy()
    for i in range(len(data[0])):
        if len(o2) > 1:
            o2_a = avg([x[i] for x in o2])
            o2_t = "1" if o2_a == 0.5 else "0" if o2_a < 0.5 else "1"
            o2 = [x for x in o2 if str(x[i]) == o2_t]
        if len(co2) > 1:
            co2_a = avg([x[i] for x in co2])
            co2_t = "0" if co2_a == 0.5 else "0" if co2_a > 0.5 else "1"
            co2 = [x for x in co2 if str(x[i]) == co2_t]
    o2 = int("".join([str(x) for x in o2[0]]),2)
    co2 = int("".join([str(x) for x in co2[0]]),2)
    return o2 * co2

if __name__ == '__main__':
    fn = 'd03eg.txt'
    fn = 'd03.txt'
    data = []
    for l in readlines(fn):
        data.append([int(i) for i in l])
    print(part1(data))
    print(part2(data))
