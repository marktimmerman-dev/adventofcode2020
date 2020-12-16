import re

prog = re.compile(r"^[\w ]+: (\d+)-(\d+) or (\d+)-(\d+)$")

blocks = open('input.txt').read().split('\n\n')

rr = []

rng = blocks[0].splitlines()
for r in rng:
    g = prog.match(r).groups()
    rr = rr + list(range(int(g[0]),int(g[1])+1))
    rr = rr + list(range(int(g[2]),int(g[3])+1))

nb = blocks[2].replace('nearby tickets:\n','').replace('\n',',').rstrip(',').split(',')
nearby = [int(x) for x in nb]

nn = []
for n in nearby:
    if n not in rr:
        nn.append(n)

print(sum(nn))
