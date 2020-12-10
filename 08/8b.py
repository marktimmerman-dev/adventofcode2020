import re
import copy

regex = r"^(\w+) \+?(\-?\d+)$"
prog = re.compile(regex)

orig_prog = [list(prog.search(line).groups()) for line in open('input.txt').read().splitlines()]

found = False

for i in range(len(orig_prog)):
    prog = copy.deepcopy(orig_prog)

    op = prog[i][0]
    if (op=='nop'):
        prog[i][0]='jmp'
    if (op=='jmp'):
        prog[i][0]='nop'
    if (op=='acc'):
        continue

    ip = 0
    a = 0

    already_executed = []
    while True:
        if ip in already_executed:
            break
        if ip >= len(prog):
            print('finished! value of accumulator is',a)
            found = True
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
    
    if found:
        break
    
