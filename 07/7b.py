import re

regex = r"^\s?(?P<amount>\d+ )?(?P<color>\w+ \w+) bags?\.?$"
prog = re.compile(regex)

graph = [];


def find_bags(color):
    print('find',color)
    c = 0
    for g in graph:
        if g[0] == color:
             print('   ', g[2], g[1])
             c = c + g[2]
             c = c + g[2]*find_bags(g[1])
    print(c)
    return c        
            
    


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        print('-----\n', line)
        fromto = line.split('contain')
        fr = fromto[0].strip()
        
        m = prog.search(fr)
        fromcolor = m.group('color')
        print(fromcolor)
        
        to = fromto[1].split(',')
        for t in to:
            if t.strip() != 'no other bags.':
                m = prog.search(t)
                tocolor = m.group('color')
                a = int(m.group('amount'))
                print(a, tocolor)
                graph.append((fromcolor, tocolor, a))

    print('==========')
    
    color = "shiny gold"
    
    bags = find_bags(color)
    print('number of bags is',bags)
    
