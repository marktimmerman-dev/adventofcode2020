import json

valid = 0

with open('input.txt', 'r+') as f:
    lines = f.read().splitlines()
    lines.append('')
    
    p=''
    
    for l in lines:
        #print(l)
        p = p+l+' '
        if l == '':
            d = "{\""+p.strip()+"\"}"
            d = d.replace(" ",",")
            d = d.replace(":","\":\"")
            d = d.replace(",","\",\"")
            passport = json.loads(d)
            print(passport.keys())
            print(len(passport))
            
            if len(passport)==8 or (not ("cid" in passport) and len(passport) == 7):
                print('valid')
                valid = valid + 1
            
            print('-----------')
            p=''

print('totaal:',valid)
