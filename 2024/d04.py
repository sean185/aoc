filename = 'd04eg.txt'
filename = 'd04.txt'
with open(filename) as f:
    txt = f.read().splitlines()
inp = [list(l) for l in txt]

def bounded(i, j, n):
    return (0 <= i <= n-1) and (0 <= j <= n-1)

n = len(inp)

# part 1
matches = ["XMAS", "SAMX"]
total = 0
for j in range(n):
    for i in range(n):
        # horizontal
        if bounded(i, j, n) and bounded(i+3, j, n):
            ss = "".join(inp[j][i:i+4])
            if ss in matches:
                total += 1
        # vertical
        if bounded(i, j, n) and bounded(i, j+3, n):
            ss = "".join([inp[j+k][i] for k in range(4)])
            if ss in matches:
                total += 1
        # diagonal-right
        if bounded(i, j, n) and bounded(i+3, j+3, n):
            ss = "".join([inp[j+k][i+k] for k in range(4)])
            if ss in matches:
                total += 1
        # diagonal-left
        if bounded(i+3, j, n) and bounded(i, j+3, n):
            ss = "".join([inp[j+k][i+3-k] for k in range(4)])
            if ss in matches:
                total += 1
print(total)

# part 2
matches = ["MAS", "SAM"]
total = 0
for j in range(n):
    for i in range(n):
        # x-shape
        if bounded(i, j, n) and bounded(i+2, j+2, n):
            dl = "".join([inp[j+k][i+k] for k in range(3)])
            dr = "".join([inp[j+2-k][i+k] for k in range(3)])
            if (dl in matches) and (dr in matches):
                total += 1
print(total)

