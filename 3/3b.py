
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def expand(s):
    r = ""
    for x in range(11 * 7):
        r = r + s
    return r

product = 1

with open('input.txt', 'r+') as f:
    map = [expand(s) for s in f.read().splitlines()]
    
    for right, down in slopes:
    
        trees = 0
        x = 0
        line = 0
        for row in map:
            line = line + 1
            if (line - 1) % down != 0:
                continue
            if x > 0:
                if row[x] == '#':
                    trees=trees+1
            x = x + right

        print('number of trees for slope right',right,'down',down,':',trees)
        product = product * trees


print('answer:', product)
