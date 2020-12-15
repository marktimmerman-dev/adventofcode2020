data = [ int(x) for x in open('example.txt').read().split(',') ]
#print(data)

def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1



while len(data) < 2020:
    last = data[-1]
    if last in data[:-1]:
        data.append(len(data)-1-(rindex(data[:-1], last)))
    else:
        data.append(0)
print(data[-1])    
    
