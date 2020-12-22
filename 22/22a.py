block = open('input.txt').read().split('\n\n')

player1 = [ int(x) for x in block[0].splitlines()[1:] ]
player2 = [ int(x) for x in block[1].splitlines()[1:] ]

while len(player1) and len(player2):
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

i = 1
score = 0
cards = player1 + player2
cards.reverse()
for c in cards:
    score = score + i * c
    i = i + 1
print(score)
