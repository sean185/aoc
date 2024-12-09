filename = "d09eg.txt"
filename = "d09.txt"
with open(filename) as f:
    txt = f.read()

def make(txt):
    isSpace = False
    res = list()
    fileid = 0
    for i in [int(x) for x in txt]:
        res += [None if isSpace else fileid for _ in range(i)]
        fileid += isSpace
        isSpace = not isSpace
    return res

def part1(res):
    while None in res:
        i = res.index(None)
        j = len(res) - 1
        if res[j] is not None:
            res[i] = res[j]
        res.pop(j)
    return res

def checksum(res):
    return sum([i*(0 if x is None else x) for i, x in enumerate(res)])

# print(checksum(part1(make(txt)))) # 18s to run wtf

def part2(res):
    for i in range(res[-1], 0, -1):
        # get size of the fileid
        old = [j for j, x in enumerate(res) if x == i]
        c = len(old)
        # check if there are any contiguous spaces available
        spaces = list()
        for j, x in enumerate(res):
            if x is None:
                spaces.append(j)
            else:
                spaces = list()
            if len(spaces) == c and spaces[-1] < old[0]:
                # perform the move if found
                res[spaces[0]:spaces[-1]+1] = [i]*c
                res[old[0]:old[-1]+1] = [None]*c
                break
    return res

# print(checksum(part2(make(txt)))) # 103s to run, horrible

# part 1 re-attempt
def part1(res):
    i = 0
    j = len(res)-1
    while i<j:
        if res[i] is None:
            if res[j] is None:
                j -= 1
                continue
            res[i] = res[j]
            res[j] = None
            i += 1
            j -= 1
        else:
            i += 1
    return res

print(checksum(part1(make(txt)))) # ok 51ms, much better

# part 2 re-attempt 
def part2(res):
    j = len(res)-1
    for FID in range(res[-1], 0, -1):
        # first build the positions of the file
        cacheF = list()
        while j > 0:
            if res[j] == FID:
                cacheF.append(j)
            elif len(cacheF) > 0:
                break
            j -= 1
        # then search for a suitable space, if any
        i = 0
        c = len(cacheF)
        cacheS = list()
        while i<=j:
            if res[i] is None:
                cacheS.append(i)
            elif c > 0 and len(cacheS) >= c:
                break
            else:
                cacheS.clear()
            i += 1
        # finally apply the swap if a suitable space was found
        if len(cacheS) >= c:
            res[cacheS[0]:cacheS[0]+c] = [FID]*c
            s = min(cacheF)
            res[s:s+c] = [None]*c
    return res

print(checksum(part2(make(txt)))) # better but still took 19s
