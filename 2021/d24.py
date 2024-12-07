from pprint import pprint 
with open('d24.txt') as f:
    instructions = f.read().splitlines()

# instructions = instructions[:2*18]
state = {(0, 0, 0, 0):''}
result = {(0, 0, 0, 0):''}

for inst in instructions:
    print(inst)
    inst = inst.split(' ')
    if inst[0] == 'inp':
        # compact results before expanding
        compact = dict()
        for v, k in state.items():
            cv = v[-1]
            if cv in compact and compact[cv] > k:
                continue
            compact[cv] = k
        print(len(compact))
        # pprint(compact)
        newstate = dict()
        for v, k in compact.items():
            for i in range(9,0,-1):
                newstate[(i,0,0,v)] = k+str(i)
        state = newstate
        continue
    op, l, r = inst
    p = 'wxyz'.index(l)
    newstate = dict()
    for v, k in state.items():
        v = list(v)
        rval = v['wxyz'.index(r)] if r in 'wxyz' else int(r)
        if op == 'add':
            if l == 'z' and rval < 0:
                print(rval)
            v[p] = v[p] + rval
        if op == 'mul':
            v[p] = v[p] * rval
        if op == 'eql':
            v[p] = int(v[p] == rval)
        if op == 'div':
            v[p] = int(v[p] / rval)
        if op == 'mod':
            v[p] = v[p] % rval
        v = tuple(v)
        if v in newstate and newstate[v] > k:
            continue
        newstate[v] = k
    state = newstate
    # print(state)

compact = dict()
for v, k in state.items():
    cv = v[-1]
    if cv in compact and compact[cv] > k:
        continue
    compact[cv] = k

print(len(compact))