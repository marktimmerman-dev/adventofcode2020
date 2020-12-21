import re


without_or = re.compile(r"^((\d+)\s?)+$")
a_or_b  =    re.compile(r"^\"([ab])\"$")

d = dict()


def build_regex(nr):
    rule = d[nr]
    s = "("
    match = a_or_b.match(rule)
    if match:
        return match.group(1)
    match =  without_or.match(rule)
    if match:
        nrs = rule.split(' ')
        for n in nrs:
            s = s + build_regex(n)
    if "|" in rule:
        left, right = rule.split("|")
        nrsleft = left.strip().split(' ')
        nrsright = right.strip().split(' ')
        s = s + "("
        for l in nrsleft:
            s = s + build_regex(l)
        s = s + r")|("
        for r in nrsright:
            s = s + build_regex(r)
        s = s + ")"
    s = s + ")"
    return s
               
        


block = open('input.txt').read().split('\n\n')

rules = block[0].splitlines()
messages = block[1].splitlines()


for r in rules:
    nr, rule = r.split(':')
    d[nr] = rule.strip()

regex = r"^" + build_regex('0') + r"$"
p = re.compile(regex)

valid_messages = [ m for m in messages if p.match(m) ]
print(len(valid_messages))
