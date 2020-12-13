import fileinput
from math import ceil

lines = [line.strip() for line in fileinput.input()]
n = int(lines[0])
xs = lines[1].split(',')

mn = float('inf')
bus_id = None
for x in xs:
    if x.isnumeric():
        x = int(x)
        if x*ceil(n/x) < mn:
            mn = x*ceil(n/x)
            bus_id = x

print((mn - n) * bus_id)

# Part 2
nums = []
for i, x in enumerate(xs):
    if x.isnumeric():
        x = int(x)
        nums.append((x, -i % x))

nums.sort(reverse=True)
i = 1
dx, x = nums[0]
while i < len(nums):
    n, a = nums[i]
    while x % n != a:
        x += dx
    dx *= n
    i += 1
print(x)

# Alternative Part 2: Put the following into https://www.dcode.fr/chinese-remainder
# for i, x in enumerate(xs):
#     if x.isnumeric():
#         x = int(x)
#         print(f'x = {-i % x}\t(mod {x})')
