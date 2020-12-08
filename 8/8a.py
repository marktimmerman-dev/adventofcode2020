import re

regex = r"^(\w+) \+?(\-?\d+)$"
prog = re.compile(regex)

prog = [prog.search(line).groups() for line in open('input.txt').read().splitlines()]

ip = 0
a = 0

already_executed = []

while True:
    if ip in already_executed:
        print('value of accumulator is',a)
        break
    already_executed.append(ip)
    op,value = prog[ip]
    if (op == 'nop'):
        ip = ip + 1
        continue
    if (op == 'jmp'):
        ip = ip + int(value)
        continue
    if (op == 'acc'):
        a = a + int(value)
        ip = ip + 1
        continue
    
