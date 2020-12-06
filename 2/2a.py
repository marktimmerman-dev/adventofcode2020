nvalid = 0

with open('input.txt', 'r+') as f:
    for line in f:
        column = line.split()
        minmax = column[0].split('-')
        min = int(minmax[0])
        max = int(minmax[1])
        letter = column[1].split(':')[0]
        password = column[2]
        
        n = password.count(letter)
        
        valid = n >= min and n <= max
        if valid:
            nvalid=nvalid+1
        
#        print(valid,min,max,letter,password,'---',line)

print('number of valid passwords:',nvalid)
