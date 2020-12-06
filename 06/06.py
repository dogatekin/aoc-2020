import fileinput
import string

groups = ''.join(list(fileinput.input())).split('\n\n')

part1 = 0
part2 = 0
for group in groups:
    yes = set()
    for answers in group.split('\n'):
        for q in answers:
            yes.add(q)
    part1 += len(yes)

    people = group.split('\n')
    for c in string.ascii_lowercase:
        if all(c in person for person in people):
            part2 += 1

print(part1)
print(part2)