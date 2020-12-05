import fileinput

passes = [line.strip() for line in fileinput.input()]

codes = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
part1 = 0
sids = []
for bp in passes:
    for old, new in codes.items():
        bp = bp.replace(old, new)

    row = int(bp[:7], 2)
    col = int(bp[-3:], 2)
    sid = row * 8 + col

    part1 = max(part1, sid)
    sids.append(sid)

print(part1)

sids.sort()
for i in range(1, len(sids)-1):
    if sids[i] != sids[i-1]+1:
        part2 = sids[i]-1

print(part2)