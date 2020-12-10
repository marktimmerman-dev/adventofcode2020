data = [int(x) for x in open('input.txt').read().splitlines() ]
data.append(0)
data.sort()

enen = 0
drieen = 1
for i in range(1, len(data)):
    diff = data[i] - data[i-1]
    if (diff == 1):
        enen = enen + 1
    if (diff == 3):
        drieen = drieen + 1
print(enen * drieen)    
