import copy
def split(word): 
    return [char for char in word]  
    
map = [split(line) for line in open('example.txt').read().splitlines()]

def print_map(map):
    for r in map:
        print("".join(r))
        

print_map(map)

rows = len(map)
cols = len(map[0])
print(rows,cols)

def adjacent(r, c):
    a = 0

    # N
    ri = r-1
    ci = c
    while ri > 0 and map[ri][ci] == '.':
        ri = ri-1
    if ri > 0 and map[ri][ci] == '#':
        a = a + 1
        
    # E
    ci = c+1
    ri = r
    while ci < cols-1 and map[ri][ci] == '.':
        ci = ci+1
    if ci < cols-1 and map[ri][ci] == '#':
        a = a + 1

    # S
    ri = r+1
    ci = c
    while ri < rows-1 and map[ri][ci] == '.':
        ri = ri+1
    if ri < rows-1 and map[ri][ci] == '#':
        a = a + 1
        
    # W
    ci = c-1
    ri = r
    while ci > 0 and map[ri][ci] == '.':
        ci = ci-1
    if ci > 0 and map[ri][ci] == '#':
        a = a + 1
    
    # NE
    ci = c+1
    ri = r-1
    while ri > 0 and ci < cols-1 and map[ri][ci] == '.':
        ci=ci+1
        ri=ri-1
    if ri > 0 and ci < cols-1 and map[ri][ci] == '#':
        a = a + 1
    
    # SE
    ci = c+1
    ri = r+1
    while ri < rows-1 and ci < cols-1 and map[ri][ci] == '.':
        ci=ci+1
        ri=ri+1
    if ri < rows-1 and ci < cols-1 and map[ri][ci] == '#':
        a = a + 1
    
    #SW
    ci = c-1
    ri = r+1
    while ri < rows-1 and ci > 0 and map[ri][ci] == '.':
        ri=ri+1
        ci=ci-1
    if ri < rows-1 and ci > 0 and map[ri][ci] == '#':
        a = a + 1
    
    # NW
    ci = c-1
    ri = r-1
    while ri > 0 and ci > 0 and map[ri][ci] == '.':
        ri=ri-1
        ci=ci-1
    if ri > 0 and ci > 0 and map[ri][ci] == '#':
        a = a + 1
    
    return a

def do_round(map):
    new_map = copy.deepcopy(map)

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 'L':
                if adjacent(r,c) == 0:
                    new_map[r][c] = '#'
            if map[r][c] == '#':
                if adjacent(r,c) >= 5:
                    new_map[r][c] = 'L'
        
    return new_map, map != new_map


while True:
    print('-----')
    map, changed = do_round(map)
    if not changed:
        break;
    print_map(map)

occupied_seats = sum([ row.count('#') for row in map])
print(occupied_seats)
