import fileinput

lines = [line.strip() for line in fileinput.input()]

rows = len(lines)
cols = len(lines[0])

r = 0
c = 0
part1 = 0
while r < rows:
    if lines[r][c % cols] == '#':
        part1 += 1
    r += 1
    c += 3
    
print(part1)
    
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
part2 = 1
for dr, dc in slopes:
    r = c = trees = 0
    while r < rows:
        if lines[r][c % cols] == '#':
            trees += 1
        r += dr
        c += dc
    part2 *= trees 

print(part2)