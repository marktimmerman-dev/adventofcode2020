import numpy as np

f = open('input.txt')

timestamp = int(f.readline())

busses = [int(bus) for bus in f.readline().split(',') if bus != 'x']

n = len(busses)

wait = (busses - np.mod(timestamp * np.ones(n, dtype=int), busses)).tolist()

m = min(wait)

b = busses[wait.index(m)]

print(b*m)
