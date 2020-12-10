with open('input.txt', 'r+') as f:
    expenses = [int(x) for x in f.read().splitlines()]
    
    for x in expenses:
        for y in expenses:
            for z in expenses:
                if x + y + z == 2020:
                    print(x,'+',y,'+',z,'=',x+y+z,'  ',x,'*',y,'*',z,'=',x*y*z)
