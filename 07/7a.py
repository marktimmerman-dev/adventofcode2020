import re

regex = r"^\s?(?P<amount>\d+ )?(?P<color>\w+ \w+) bags?\.?$"
prog = re.compile(regex)

graph = [];


def find_containers(color):
    print('find',color)
    c = set([])
    for g in graph:
        if g[1] == color:
            c.add(g[0])
            c.update(find_containers(g[0]))
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
                print(m.group('amount'), tocolor)
                graph.append((fromcolor, tocolor))

    print('==========')
    
    color = "shiny gold"
    
    colors = find_containers(color)
    print(colors)
    print('number of colors is',len(colors))
    
