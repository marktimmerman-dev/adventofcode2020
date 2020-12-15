import re

rmask = re.compile(r"^mask = ([01X]+)$")
rmem = re.compile(r"^mem\[(\d+)\] = (\d+)")

program = open('input.txt').read().splitlines()

mem = dict()

mask = 0
mval = 0

for line in program:
    if rmask.match(line):
        m = rmask.match(line).group(1)
        mask = int(m.replace('1','0').replace('X','1'),2)
        mval = int(m.replace('X','0'),2)
    else:
        addr, value = rmem.match(line).groups()
        value = int(value)
        addr = int(addr)
        result = mval + (value & mask)
        mem[addr] = result

print(sum(mem.values()))
