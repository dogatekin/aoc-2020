import fileinput
from itertools import product
from collections import defaultdict

lines = [list(line.strip()) for line in fileinput.input()]
deltas = [d for d in product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]

def neighbours(x, y, z):
    return [(x+dx, y+dy, z+dz) for dx, dy, dz in deltas]    

n = len(lines)
grid = defaultdict(lambda: '.')
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            grid[0, y-n//2, x-n//2] = lines[y][x]

for _ in range(6):
    n += 2
    add = []
    rem = []
    for x, y, z in product(range(-(n//2), n//2+1), repeat=3):
        if grid[x,y,z] == '.' and sum(grid[nx,ny,nz]=='#' for nx,ny,nz in neighbours(x,y,z)) == 3:
            add.append((x,y,z))       
        elif grid[x,y,z] == '#' and not (2 <= sum(grid[nx,ny,nz]=='#' for nx,ny,nz in neighbours(x,y,z)) <= 3):
            rem.append((x,y,z))

    for x, y, z in add:
        grid[x,y,z] = '#'
    for x, y, z in rem:
        grid[x,y,z] = '.'

print(sum(v == '#' for v in grid.values()))

deltas = [d for d in product((-1, 0, 1), repeat=4) if d != (0, 0, 0, 0)]

def neighbours_4(x, y, z, w):
    return [(x+dx, y+dy, z+dz, w+dw) for dx, dy, dz, dw in deltas]    

n = len(lines)
grid = defaultdict(lambda: '.')
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            grid[0, 0, y-n//2, x-n//2] = lines[y][x]

for i in range(6):
    n += 2
    add = []
    rem = []
    for x, y, z, w in product(range(-(n//2), n//2+1), repeat=4):
        if grid[x,y,z,w] == '.' and sum(grid[nx,ny,nz,nw]=='#' for nx,ny,nz,nw in neighbours_4(x,y,z,w)) == 3:
            add.append((x,y,z,w))       
        elif grid[x,y,z,w] == '#' and not (2 <= sum(grid[nx,ny,nz,nw]=='#' for nx,ny,nz,nw in neighbours_4(x,y,z,w)) <= 3):
            rem.append((x,y,z,w))

    for x, y, z, w in add:
        grid[x,y,z,w] = '#'
    for x, y, z, w in rem:
        grid[x,y,z,w] = '.'

print(sum(v == '#' for v in grid.values()))