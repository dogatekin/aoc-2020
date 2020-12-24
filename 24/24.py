import fileinput
from collections import defaultdict

d = {
    'e': (1, 0),
    'se': (0, 1),
    'sw': (-1, 1),
    'w': (-1, 0),
    'nw': (0, -1),
    'ne': (1, -1)
    }

blacks = set()

for line in fileinput.input():
    line = line.strip()
    x = y = 0
    i = 0 
    while i < len(line):
        c = line[i]
        if c in d:
            dx, dy = d[c]
            i += 1
        else:
            dx, dy = d[line[i:i+2]]
            i += 2
        x += dx
        y += dy
    if (x, y) in blacks:
        blacks.remove((x, y))
    else:
        blacks.add((x, y))

print(len(blacks))

for _ in range(100):
    rem = []
    whites = defaultdict(int)
    for x, y in blacks:
        nbours = 0
        for dx, dy in d.values():
            if (x+dx, y+dy) in blacks:
                nbours += 1
            else:
                whites[x+dx, y+dy] += 1
        if nbours == 0 or nbours > 2:
            rem.append((x, y))

    for tile in rem:
        blacks.remove(tile)

    for tile, nbours in whites.items():    
        if nbours == 2:
            blacks.add(tile)

print(len(blacks))