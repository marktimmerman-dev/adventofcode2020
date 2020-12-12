data = [ (line[0], int(line[1:])) for line in open('input.txt').read().splitlines()  ]

direction = [ 'N','E','S','W' ]
direction2xy = { 'N': (1,0), 'E': (0,1), 'S': (-1,0), 'W': (0,-1) }
heading2direction = { 0: 'N', 90: 'E', 180: 'S', 270: 'W'}

x = 0 # easting
y = 0 # northing
heading = 90
d = heading2direction[heading]

for cmd,value in data:
    if cmd in direction:
        vx, vy = direction2xy[cmd]
        x = x + value * vx
        y = y + value * vy
    if cmd == 'F':
        vx, vy = direction2xy[d]
        x = x + value * vx
        y = y + value * vy
    if cmd == 'R':
        heading = (heading + value) % 360
        d = heading2direction[heading]
    if cmd == 'L':
        heading = (360 + heading - value) % 360
        d = heading2direction[heading]

print(abs(x)+abs(y))
