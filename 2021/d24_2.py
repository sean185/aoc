from pprint import pprint
v1 = (12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12)
v2 = (1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26)
v3 = (6, 2, 13, 8, 13, 8, 3, 11, 10, 8, 14, 6, 8, 2)

def step(z, w, i):
    if w == z % 26 + v1[i]:
        return z//v2[i]
    else:
        return 26 * z//v2[i] + w + v3[i]

def step14(inputs):
    # step14("99298993199873")
    z = 0
    for i in range(14):
        w = int(inputs[i])
        z = step(z, w, i)
        print(z)
    return z

def back(z, w, i):
    zs = []
    p2 = z - v3[i] - w
    # zb = 26 * z//v2[i] + w + v3[i]
    # zb - w - v3[i] = 26 * z//v2[i]
    # (zb - w - v3[i])//26*v2[i] = z
    if p2%26 == 0:
        zs.append(p2//26 * v2[i])
    # zb = z//v2[i] when w == z % 26 + v1[i]
    # zb*v2[i] = z when w - v1[i] == z % 26
    # zb*v2[i] = z when 0 <= w - v1[i] < 26
    if 0 <= w - v1[i] < 26:
        zs.append(w - v1[i] + z * v2[i])
    return zs

zs = {0}
result = {}
for i in range(13, -1, -1):
    newzs = set()
    for w in range(9, 0, -1):
    # for w in range(1, 10):
        for z in zs:
            for x in back(z, w, i):
                newzs.add(x)
                result[x] = (w,) + result.get(z, ())
    zs = newzs

print(''.join(str(digit) for digit in result[0]))

