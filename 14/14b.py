import re
import numpy as np

rmask = re.compile(r"^mask = ([01X]+)$")
rmem = re.compile(r"^mem\[(\d+)\] = (\d+)")

program = open('input.txt').read().splitlines()

mem = dict()

mask = 0
mval = 0
xmask = 0
x = []
comb = []

def combinations(v):
    c = []
    for i in range(1 << len(v)):
        k = 0
        for j in range(len(v)):
            if i & (1 << j):
                k = k + (1 << v[j])
        c.append(k)    
    c.sort()
    return c
    
for line in program:
    if rmask.match(line):
        m = rmask.match(line).group(1)
        mask = int(m.replace('X', '0'),2)
        xmask = int(m.replace('0','1').replace('X','0'),2)
        x = (35-np.where(np.array([char for char in m]) == 'X')[0]).tolist()
        comb = combinations(x) 

    else:
        addr, value = rmem.match(line).groups()
        value = int(value)
        addr = int(addr)
        
        newaddr = addr | mask
                
        
        for c in comb:
            actual = (newaddr & xmask) | c
            mem[actual] = value

print(sum(mem.values()))
