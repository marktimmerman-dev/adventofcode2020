import copy
def split(word): 
    return [char for char in word]  
    
map = [split(line) for line in open('input.txt').read().splitlines()]

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
    if r > 0 and map[r-1][c] == '#':
        a = a + 1
    # E
    if c < cols-1 and map[r][c+1] == '#':
        a = a + 1
    # S
    if r < rows-1 and map[r+1][c] == '#':
        a = a + 1
    # W
    if c > 0 and map[r][c-1] == '#':
        a = a + 1
    # NE
    if r > 0 and c < cols-1 and map[r-1][c+1] == '#':
        a = a + 1
    # SE
    if r < rows-1 and c < cols-1 and map[r+1][c+1] == '#':
        a = a + 1
    #SW
    if r < rows-1 and c > 0 and map[r+1][c-1] == '#':
        a = a + 1
    # NW
    if r > 0 and c > 0 and map[r-1][c-1] == '#':
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
                if adjacent(r,c) >= 4:
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
