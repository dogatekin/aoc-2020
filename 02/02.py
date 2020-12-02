import fileinput

part1 = 0
part2 = 0
for line in fileinput.input():
    allowed, c, pwd = line.split()
    mn, mx = map(int, allowed.split('-'))
    c = c[0]
    
    if mn <= pwd.count(c) <= mx:
        part1 += 1
        
    if (pwd[mn-1] == c or pwd[mx-1] == c) and not (pwd[mn-1] == c and pwd[mx-1] == c):
        part2 += 1

print(part1)
print(part2)