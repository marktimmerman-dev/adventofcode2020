data = [ int(x) for x in open('input.txt').read().split(',') ]

previous = dict()


for i in range(len(data)-1):
    previous[data[i]] = i
    

last = data[-1]
i = len(data)-1

while i < 30000000-1:
    if last in previous:
        next = i - previous[last]
        previous[last] = i
    else:
        previous[last] = i
        next = 0
    last = next
    i = i + 1
print(last)
