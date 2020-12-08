import fileinput

instructions = [line.strip() for line in fileinput.input()]

def run():
    acc = 0
    ptr = 0
    seen = [False]*len(instructions)
    while ptr < len(instructions) and not seen[ptr]:
        seen[ptr] = True
        ins, offset = instructions[ptr].split()
        offset = int(offset)
        
        if ins == 'acc':
            acc += offset
            ptr += 1
        elif ins == 'jmp':
            ptr += offset
        elif ins == 'nop':
            ptr += 1
    if ptr < len(instructions):
        return False, acc
    else:
        return True, acc

part1 = run()[1]
print(part1)

nops = [i for i, ins in enumerate(instructions) if ins.startswith('nop')]
for ind in nops:
    old = instructions[ind]
    new = "jmp" + old[3:]
    instructions[ind] = new
    finished, acc = run()
    if finished:
        part2 = acc
    instructions[ind] = old
        
jmps = [i for i, ins in enumerate(instructions) if ins.startswith('jmp')]
for ind in jmps:
    old = instructions[ind]
    new = "nop" + old[3:]
    instructions[ind] = new
    finished, acc = run()
    if finished:
        part2 = acc
    instructions[ind] = old

print(part2)