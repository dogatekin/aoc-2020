import fileinput
from collections import defaultdict, deque

lines = [line.strip() for line in fileinput.input()]

candidates = {}
for line in lines:
    ingredients, allergens = line.split(' (contains ')
    for allergen in allergens[:-1].split(', '):
        if allergen not in candidates:
            candidates[allergen] = set(ingredients.split())
        else:
            candidates[allergen] &= set(ingredients.split())

queue = deque()
found = set()
for allergen, possibilities in candidates.items():
    if len(possibilities) == 1:
        queue.append((allergen, next(iter(possibilities))))
        found.add(allergen)
        
while queue:
    allergen, ingredient = queue.popleft()
    for allerg in candidates:
        if allerg not in found:
            candidates[allerg].discard(ingredient)
            if len(candidates[allerg]) == 1:
                queue.append((allerg, next(iter(candidates[allerg]))))
                found.add(allerg)

identified = set()
for ingredient in candidates.values():
    identified |= ingredient

cnt = 0
for line in lines:
    ingredients, allergens = line.split(' (contains ')
    for ingredient in ingredients.split():
        if ingredient not in identified:
            cnt += 1
print(cnt)

identified = {}
for allergen, ingredients in candidates.items():
    identified[next(iter(ingredients))] = allergen

print(','.join(sorted(identified.keys(), key=lambda k: identified[k])))