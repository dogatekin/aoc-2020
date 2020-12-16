import fileinput
from collections import deque

lines = list(fileinput.input())

rules, mine, nearby = ''.join(lines).split('\n\n')

ranges = {}
for rule in rules.splitlines():
    field, r1, _, r2 = rule.split()
    ranges[field[:-1]] = [tuple(map(int, r.split('-'))) for r in (r1, r2)]

tickets = []
total = 0
for ticket in nearby.splitlines()[1:]:
    values = tuple(map(int, ticket.split(',')))
    valid = True
    
    for value in values:
        if any(mn <= value <= mx for field in ranges for mn, mx in ranges[field]):
            continue
        else:
            total += value
            valid = False
    
    if valid:
        tickets.append(values)

print(total)

tickets.append(tuple(map(int, mine.splitlines()[1].split(','))))

def is_valid(value, field):
    return any(mn <= value <= mx for mn, mx in ranges[field])

candidates = [set(ranges) for _ in range(len(ranges))]

for ticket in tickets:
    for i, val in enumerate(ticket):
        possible = {field for field in ranges if is_valid(val, field)}
        candidates[i] &= possible

queue = deque([i for i, cand in enumerate(candidates) if len(cand)==1])

while queue:
    cur = queue.pop()
    for i in range(len(candidates)):
        if len(candidates[i]) > 1:
            candidates[i] -= candidates[cur]
            if len(candidates[i]) == 1:
                queue.append(i)

fields = [cand.pop() for cand in candidates]
my_ticket = tickets[-1]

out = 1
for field, val in zip(fields, my_ticket):
    if field.startswith('departure'):
        out *= val

print(out)