import fileinput
from itertools import product
from collections import defaultdict

seats = [list(line.strip()) for line in fileinput.input()]
m = len(seats)
n = len(seats[0])

init_seats = [row.copy() for row in seats]

# Part 1
def new_seat(seats, r, c):
    neighbours = [(r+dr, c+dc) for dr, dc in product((-1,0,1), (-1,0,1)) if (dr, dc) != (0, 0)]
    neighbours = [(r, c) for r, c in neighbours if 0 <= r < m and 0 <= c < n]
    
    if seats[r][c] == 'L' and all(seats[r][c] != '#' for r, c in neighbours):
        return '#'
    elif seats[r][c] == '#' and sum(seats[r][c] == '#' for r, c in neighbours) >= 4:
        return 'L'
    else:
        return seats[r][c]

old_seats = None
while seats != old_seats:
    old_seats = [row.copy() for row in seats]
    
    for r in range(m):
        for c in range(n):
            seats[r][c] = new_seat(old_seats, r, c)

print(sum(row.count("#") for row in seats))


# Part 2
seats = init_seats
neighbours = defaultdict(list)
directions = [(dr, dc) for dr, dc in product((-1,0,1), (-1,0,1)) if (dr, dc) != (0, 0)]
for r in range(m):
    for c in range(n):
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            while 0 <= nr < m and 0 <= nc < n:
                if seats[nr][nc] == '.':
                    nr += dr
                    nc += dc
                else:
                    neighbours[r, c].append((nr, nc))
                    break
                
def new_seat_2(seats, r, c):
    if seats[r][c] == 'L' and all(seats[nr][nc] == 'L' for nr, nc in neighbours[r, c]):
        return '#'
    elif seats[r][c] == '#' and sum(seats[nr][nc] == '#' for nr, nc in neighbours[r, c]) >= 5:
        return 'L'
    else:
        return seats[r][c]

old_seats = None
while seats != old_seats:
    old_seats = [row.copy() for row in seats]
    
    for r in range(m):
        for c in range(n):
            seats[r][c] = new_seat_2(old_seats, r, c)

print(sum(row.count("#") for row in seats))