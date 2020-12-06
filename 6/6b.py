with open('input.txt', 'r+') as f:
    groups = f.read().split("\n\n")
    sum_of_count = 0
    for g in groups:
        print('---')
        persons = g.split("\n")
        print(persons)
        s = set('abcdefghijklmnopqrstuvwxyz')
        for p in persons:        
            t = set(p)
            if len(t) > 0:
                s = s.intersection(t)
        count = len(s)
        print(count)
        sum_of_count = sum_of_count + count
print(sum_of_count)
        


    
