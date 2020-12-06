trees = 0

def expand(s):
    r = ""
    for x in range(11 * 3):
        r = r + s
    return r


with open('input.txt', 'r+') as f:
    map = [expand(s) for s in f.read().splitlines()]
    
    x = 0
    for row in map:
        if x > 0:
            if row[x] == '#':
                trees=trees+1
        x = x + 3
        

print('number of trees:',trees)
