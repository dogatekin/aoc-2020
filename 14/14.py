import fileinput

lines = [line.strip() for line in fileinput.input()]
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
        m = {}
        for i, v in enumerate(mask):
            if v != 'X':
                m[i] = v
    else:
        ins, val = line.split(' = ')
        addr = ins[ins.index('[')+1:-1]
        addr, val = int(addr), int(val)
        
        bin_val = list(f"{val:#037b}")
        for i, v in m.items():
            bin_val[i+1] = v
        masked = int(''.join(bin_val), 2)

        mem[addr] = masked

print(sum(mem.values()))

def candidates(addr_str):
    if 'X' not in addr_str:
        yield int(addr_str, 2)
    else:
        yield from candidates(addr_str.replace('X', '1', 1))
        yield from candidates(addr_str.replace('X', '0', 1))

mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    else:
        ins, val = line.split(' = ')
        addr = ins[ins.index('[')+1:-1]
        addr, val = int(addr), int(val)

        bin_addr = list(f"{addr:#037b}")        
        for i, v in enumerate(mask):
            if v != '0':
                bin_addr[i+1] = v
        joined = ''.join(bin_addr)
        
        for addr in candidates(joined):
            mem[addr] = val

print(sum(mem.values()))