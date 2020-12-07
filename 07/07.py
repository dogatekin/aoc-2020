import fileinput
from collections import defaultdict, deque

contained_in = defaultdict(list)
contains = defaultdict(list)

for line in fileinput.input():
    bag, holds = line.split(" contain ")
    bag = bag[:-5]
    holds = holds.strip()[:-1].split(', ')
    for contained in holds:
        if contained != 'no other bags':
            info = contained[:contained.index('bag')]
            cnt = info[:info.index(' ')]
            color = info[info.index(' ')+1:-1]
            contained_in[color].append(bag)
            contains[bag].append((int(cnt), color))

seen = {"shiny gold"}
queue = deque(contained_in["shiny gold"])

part1 = 0
while queue:
    cur = queue.popleft()
    if cur not in seen:
        part1 += 1
        seen.add(cur)
        for bag in contained_in[cur]:
            queue.append(bag)

print(part1)

# Part 2    
def count_bags(bag):
    total = 0
    for cnt, inner_bag in contains[bag]:
        total += cnt * (1 + count_bags(inner_bag))
    return total

part2 = count_bags("shiny gold")
print(part2)