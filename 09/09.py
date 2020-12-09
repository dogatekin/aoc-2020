import fileinput

numbers = list(map(int, fileinput.input()))

preamble = 25
ind = preamble

def twosum(numbers, ind, preamble):
    target = numbers[ind]
    seen = set()
    for n in numbers[ind-preamble:ind]:
        if target - n in seen:
            return True
        seen.add(n)
    return False

while twosum(numbers, ind, preamble):
    ind += 1

part1 = numbers[ind]
print(part1)

rs = [0]
s = 0
for n in numbers:
    s += n
    rs.append(s)

target = part1
seen = {}
for i, s in enumerate(rs):
    if s - target in seen and seen[s-target] != i-1:
        group = numbers[seen[s-target]:i]
        part2 = min(group)+max(group)
        break
    seen[s] = i

print(part2)
