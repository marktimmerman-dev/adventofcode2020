nvalid = 0

with open('input.txt', 'r+') as f:
    for line in f:
        column = line.split()
        positions = column[0].split('-')
        pos1 = int(positions[0])
        pos2 = int(positions[1])
        letter = column[1].split(':')[0]
        password = column[2]

        valid = (password[pos1-1] == letter and password[pos2-1] != letter) or (password[pos1-1] != letter and password[pos2-1] == letter)
        if valid:
            nvalid=nvalid+1
        
print('number of valid passwords:',nvalid)
