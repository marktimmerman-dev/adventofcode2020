data = [ int(x) for x in open('input.txt').read().splitlines() ]

preamblelen = 25

gevonden = 0

def zoek(i):
    for a in range(i-preamblelen, i):
        for b in range(i-preamblelen, i):
            if data[a]+data[b]==data[i]:
                return True
    return False

for i in range(preamblelen, len(data)):
    if not zoek(i):
        print('eerste die niet voldoet:', data[i])
        gevonden = data[i]
        break

for x in range(len(data)):
    for y in range(x+1,len(data)+1):
        segment = data[x:y]
        if len(segment)>1 and sum(segment) == gevonden:
            print(min(segment)+max(segment))
                
            
