from pprint import pprint 
fn = 'd08eg.txt'
fn = 'd08.txt'
with open(fn) as f:
    txt = f.read().splitlines()

def part1():
    counter = 0
    for l in txt:
        c = [len(x) for x in l.split(' | ')[1].split(' ')]
        counter += len([x for x in c if x in (2, 3, 4, 7)])
    return counter

print(part1())

def part2():
    ans = 0
    for l in txt:
        observations, digits = l.split(' | ')
        observations = [set(x) for x in observations.split(' ')]
        mapping = dict()
        backmapping = dict()
        fives = list()
        sixes = list()
        for o in observations:
            k = ''.join(sorted(o))
            if len(o) == 2:
                mapping[1] = o
                backmapping[k] = 1
            elif len(o) == 3:
                mapping[7] = o
                backmapping[k] = 7
            elif len(o) == 4:
                mapping[4] = o
                backmapping[k] = 4
            elif len(o) == 5:
                fives.append(o)
            elif len(o) == 6:
                sixes.append(o)
            elif len(o) == 7:
                mapping[8] = o
                backmapping[k] = 8
        for f in fives:
            # 2 3 5
            k = ''.join(sorted(f))
            if len(f.intersection(mapping[1])) == 2:
                backmapping[k] = 3
            else:
                if len(f.difference(mapping[4])) == 2:
                    backmapping[k] = 5
                else:
                    backmapping[k] = 2
        for s in sixes:
            # 0 6 9
            k = ''.join(sorted(s))
            if len(s.union(mapping[1])) == 7:
                backmapping[k] = 6
            else:
                if len(s.union(mapping[4])) == 7:
                    backmapping[k] = 0
                else:
                    backmapping[k] = 9
        nums = [backmapping[''.join(sorted(x))] for x in digits.split(' ')]
        ans += int(''.join([str(x) for x in nums]))
    return ans

print(part2())