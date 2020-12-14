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
        
        X_inds = [i for i, v in enumerate(bin_addr) if v == 'X']
        bits = [f'{i:#0{len(X_inds)+2}b}'[2:] for i in range(2**len(X_inds))]
        
        for bit in bits:
            for i, v in zip(X_inds, bit):
                bin_addr[i] = v
            addr = int(''.join(bin_addr), 2)
            mem[addr] = val

print(sum(mem.values()))