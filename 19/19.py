import fileinput
from collections import defaultdict, deque
from itertools import product

rule_lines, messages = ''.join(fileinput.input()).split('\n\n')

templates = defaultdict(list)
rules = defaultdict(set)
affects = defaultdict(set)
depends_on = defaultdict(set)
for rule_line in rule_lines.splitlines():
    affected, affectors = rule_line.split(':')
    for affector_group in affectors.split('|'):
        templates[affected].append(affector_group.split())
        for affector in affector_group.split():
            if affector == '"a"':
                rules[affected].add('a')
                break
            elif affector == '"b"':
                rules[affected].add('b')
                break
            affects[affector].add(affected)
            depends_on[affected].add(affector)
            
# print(templates)
# print(rules)
# print(affects)
# print(depends_on)

queue = deque(rules)
while queue:
    cur_rule = queue.pop()
    for rule in affects[cur_rule]:
        # if rule not in ['8', '11']:
        depends_on[rule].remove(cur_rule)
        if len(depends_on[rule]) == 0:
            matches = set()
            for group in templates[rule]:
                match = product(*[rules[g] for g in group])
                for pair in match:
                    matches.add(''.join(pair))
            rules[rule] = matches
            queue.append(rule)

print(sum(message in rules['0'] for message in messages.splitlines()))

# 0 : 8 11
# 8 : 42 | 42 8
# 11: 42 31 | 42 11 31
# e.g. 42 42 42 42 42 31 31

len42 = len(next(iter(rules['42'])))

# A and B don't intersect
def valid(msg, A, B):
    '''Match AB AAB AABB AAAB...'''
    A_matches = 0
    B_matches = 0
    for i in range(0, len(msg), len42):
        group = msg[i:i+len42]
        
        if group in A and B_matches > 0:
            return False
        elif group in A and B_matches == 0:
            A_matches += 1
        elif group in B:
            B_matches += 1
        else:
            return False
    
    return B_matches > 0 and A_matches > B_matches

print(sum(valid(message, rules['42'], rules['31']) for message in messages.splitlines()))
