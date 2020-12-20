import fileinput
from math import sqrt
from collections import defaultdict, deque
import pickle

tiles = {}
tile_lines = ''.join(fileinput.input()).split('\n\n')
for tile_line in tile_lines:
    lines = tile_line.splitlines()
    tiles[int(lines[0].split()[1][:-1])] = list(map(list, lines[1:]))

def flip(tile):
    return [list(reversed(row)) for row in tile]

def rotations(tile):
    rot90 = list(zip(*tile[::-1]))
    rot180 = list(zip(*rot90[::-1]))
    rot270 = list(zip(*rot180[::-1]))
    return tile, rot90, rot180, rot270

def transforms(tile):
    return rotations(tile) + rotations(flip(tile))

# m x m grid of n x n tiles
m = int(sqrt(len(tiles)))
n = len(tiles[next(iter(tiles))])

def match_side(t1, t2, side):
    '''side of t1 to match: 0:left, 1:up, 2:right, 3:down'''
    if side == 0:
        return all(t1[i][0] == t2[i][n-1] for i in range(n))
    elif side == 1:
        return all(t1[0][i] == t2[n-1][i] for i in range(n))
    elif side == 2:
        return all(t1[i][n-1] == t2[i][0] for i in range(n))
    else:
        return all(t1[n-1][i] == t2[0][i] for i in range(n))

def match(t1, t2):
    return any(match_side(t1, t2, i) for i in range(4))

all_ids = list(tiles.keys())
adj = defaultdict(set)

p1 = 1
for t1_id in all_ids:
    t1 = tiles[t1_id]
    for t2_id in all_ids:
        if t2_id != t1_id and t2_id not in adj[t1_id]:
            t2 = tiles[t2_id]
            for transform in transforms(t2):
                if match(t1, transform):
                    adj[t1_id].add(t2_id)
                    adj[t2_id].add(t1_id)
                    break

for tid in all_ids:
    if len(adj[tid]) == 2:
        corner = tid
        p1 *= tid
print(p1)

grid = [[None for _ in range(m)] for _ in range(m)]
ids = [[None for _ in range(m)] for _ in range(m)]

queue = deque([(corner, flip(tiles[corner]), 0, 0)])
# queue = deque([(corner, tiles[corner], 0, 0)])   # might need to try this too
seen = set()
i = 0
while queue:
    tid, tile, r, c = queue.popleft()
    grid[r][c] = tile
    ids[r][c] = tid
    seen.add(tid)
    
    for nid in adj[tid]:
        if nid not in seen:
            neighbour = tiles[nid]
            for transform in transforms(neighbour):
                if match_side(tile, transform, 2):
                    queue.append((nid, transform, r, c+1))
                    break
                elif match_side(tile, transform, 3):
                    queue.append((nid, transform, r+1, c))
                    break
    i += 1
    if i == 100000000:
        print('Q: ', queue)
        break

trim_grid = [[None for _ in range(m)] for _ in range(m)]
for r in range(m):
    for c in range(m):
        trim_grid[r][c] = [row[1:-1] for row in grid[r][c][1:-1]]

n = len(trim_grid[0][0])
image = [['.' for _ in range(m*n)] for _ in range(m*n)]

for r in range(m):
    for c in range(m):
        for i in range(n):
            for j in range(n):
                image[r*n + i][c*n + j] = trim_grid[r][c][i][j]

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
monster = [list(row) for row in monster.splitlines()]

mm = len(monster)
mn = len(monster[0])

monster_parts = {(r, c) for r in range(mm) for c in range(mn) if monster[r][c] == '#'}

im = len(image)

for img in transforms(image):
    num_monsters = 0
    for r in range(im):
        for c in range(im):
            if r < im - mm and c < im - mn:
                if all(img[r+dr][c+dc] == '#' for dr, dc in monster_parts):
                    num_monsters += 1
    if num_monsters > 0:
        print(sum(img[r][c] == '#' for r in range(im) for c in range(im)) - num_monsters * len(monster_parts))