import json
import re

haircolor_regex = r"^#[0-9a-f]{6}$"
haircolor_prog =  re.compile(haircolor_regex)

eye_prog = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
pid_prog = re.compile(r"^[0-9]{9}$")


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
            print(passport)
            print(len(passport))
            
            if len(passport)==8 or (not ("cid" in passport) and len(passport) == 7):
                print('valid under 4a rules. now checking 4b rules.')
                
                byr = int(passport['byr'])
                byr_valid = byr >= 1920 and byr <= 2002
                print('byr_valid',byr_valid)
                
                iyr = int(passport['iyr'])
                iyr_valid = iyr >= 2010 and iyr <= 2020
                print('iyr_valid',iyr_valid)
                
                eyr = int(passport['eyr'])
                eyr_valid = eyr >=2020 and eyr <= 2030
                print('eyr_valid',eyr_valid)
                
                hgt = passport['hgt']
                hgt_valid = False
                if hgt.endswith('cm') or hgt.endswith('in'):
                    hgt = hgt.replace("cm"," cm")       # dit kan vast mooier met een regexp (-:
                    hgt = hgt.replace("in", " in")
                    height, unit = hgt.split()
                    h = int(height)
                    hgt_valid = (unit == 'cm' and h >= 150 and h <= 193) or (unit == 'in' and h >= 59 and h <76)
                print('hgt_valid',hgt_valid)

                hcl = passport['hcl']
                hcl_valid = haircolor_prog.match(hcl) != None
                print('hcl_valid',hcl_valid)
                
                ecl = passport['ecl']
                ecl_valid = eye_prog.match(ecl) != None
                print('ecl_valid',ecl_valid)
                
                pid = passport['pid']
                pid_valid = pid_prog.match(pid) != None
                print('pid_valid',pid_valid)
                
                


                if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
                    print('valid')
                    valid = valid + 1
            
            print('-----------')
            p=''

print('totaal:',valid)
