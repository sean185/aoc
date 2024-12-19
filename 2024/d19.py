filename = "d19eg.txt"
filename = "d19.txt"
with open(filename) as f:
    txt = f.read().splitlines()

towels = txt[0].split(", ")
designs = txt[2:]

# part 1 - keep only the combination not the permutation
total = 0
for design in designs:
    poss = set([""]) # initial condition
    for i, letter in enumerate(design):
        newposs = set()
        for p in poss:
            if len(p) > i:
                if design[:len(p)] == p:
                    newposs.add(p)
            else:
                for t in towels:
                    if t[0] == letter:
                        potential = p+t
                        if design[:len(potential)] == potential:
                            newposs.add(potential)
        poss = newposs.copy()
        if len(poss) == 0:
            break
        if design in poss:
            total += 1
            break

print(total)

# part 2 - use a dict!
total = 0
for design in designs:
    poss = { "": 1 } # initial condition
    for i, letter in enumerate(design):
        newposs = {}
        for p, c in poss.items():
            if len(p) > i:
                if design[:len(p)] == p:
                    newposs[p] = newposs.get(p, 0) + c # existing possibility survives 
            else:
                for t in towels:
                    if t[0] == letter:
                        potential = p+t
                        if design[:len(potential)] == potential:
                            newposs[potential] = newposs.get(potential, 0) + c
        poss = newposs.copy()
        if len(poss) == 0:
            break
    if design in poss:
        total += poss[design]

print(total)

