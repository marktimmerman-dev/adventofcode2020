with open('input.txt', 'r+') as f:
    expenses = [int(x) for x in f.read().splitlines()]
    
    for x in expenses:
        for y in expenses:
            if x + y == 2020:
                print(x,'+',y,'=',x+y,'  ',x,'*',y,'=',x*y)
