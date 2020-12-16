import re

prog = re.compile(r"^[\w ]+: (\d+)-(\d+) or (\d+)-(\d+)$")

blocks = open('input.txt').read().split('\n\n')

rr = []

rng = blocks[0].splitlines()
for r in rng:
    g = list(map(int, prog.match(r).groups()))
    rr = rr + list(range(g[0],g[1]+1))
    rr = rr + list(range(g[2],g[3]+1))

nearby = list(map(int, blocks[2].replace('nearby tickets:\n','').replace('\n',',').rstrip(',').split(',')))

nn = []
for n in nearby:
    if n not in rr:
        nn.append(n)

print(sum(nn))
