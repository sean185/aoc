def parse_food(l):
    ingredients, allergens = l.split(' (contains ')
    ingredients = ingredients.split()
    allergens = allergens[:-1].split(', ')
    return ingredients, allergens

with open('day21eg.txt') as f:
# with open('day21.txt') as f:
    data = f.read().splitlines()

foods = [parse_food(d) for d in data]

all_allergens = set()
for f in foods:
    all_allergens.update(f[1])

traitors = []
while len(all_allergens) > 0:
    for allg in all_allergens:
        # find ingredients containing allergens with overlaps
        subset = [f[0] for f in foods if allg in f[1]]
        ing_overlap = set(subset[0])
        for ings in subset[1:]:
            ing_overlap = ing_overlap.intersection(set(ings))
        if len(ing_overlap) > 1:
            # not yet found a unique ingredient which is an allergen
            continue
        traitor = ing_overlap.pop()
        print(allg, traitor)
        traitors.append((allg, traitor))
        # remove this allergen for sure
        for f in foods:
            if traitor in f[0]:
                f[0].remove(traitor)
    all_allergens.difference_update(set([t[0] for t in traitors]))

print(sum([len(f[0]) for f in foods]))

# part 2
traitors.sort()
print(','.join([t[1] for t in traitors]))
