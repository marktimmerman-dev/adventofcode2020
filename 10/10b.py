import numpy as np

data = [int(x) for x in open('input.txt').read().splitlines() ]
data.append(0)
data.append(max(data)+3)
data.sort()

diff = []
for i in range(1, len(data)):
    diff.append(data[i] - data[i-1])

pipo = [0,0,2,4,7]

reeks = []
i=0
while i<len(diff)-1:
    for j in range(i,len(diff)):
        if diff[j] == 3:
            if j - i > 1:
                reeks.append(pipo[j - i])
                i = j - 1
            break;
    i = i + 1
print(np.prod(reeks))
