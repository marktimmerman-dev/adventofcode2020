import numpy as np

data = [int(x) for x in open('example.txt').read().splitlines() ]
data.append(0)
data.sort()
data.append(data[-1]+3)

diff = np.diff(data).tolist()
print(diff.count(1) * diff.count(3))    
