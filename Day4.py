import re

r = re.compile(r'^[a-f][0-9]')
with open('Day4.txt') as file:  # Read stream
    content = file.read()
lines = content.split('\n\n')  # split content to lines
passports = []
diction = {}
for item in lines:
    passports.append(item.replace('\n', ' '))

counter = 0
validpass = []
for passport in passports:
    l = passport.split()
    if len(l) != 8:
        if len(l) == 7:
            diction = {}
            for i in l:
                diction.update({i.split(':')[0]: i.split(':')[1]})
            if 'cid' in diction.keys():
                continue
            else:
                counter += 1
                validpass.append(passport)
    else:
        counter += 1
        validpass.append(passport)
print(counter)
print(validpass)

RESS = 0
res = []
for valid in validpass:
    diction = {}
    for i in valid.split():
        diction.update({i.split(':')[0]: i.split(':')[1]})

    # if 1920<=int(diction['byr'])<=2002 and 2010<=int(diction['iyr'])<=2020 and 2020<=int(diction['eyr'])<=2030:
    #     if diction['hgt'].endswith('cm') and 150<=int(diction['hgt'][:len(diction['hgt'])-2])<=193 or diction['hgt'].endswith('in') and 59<=int(diction['hgt'][:len(diction['hgt'])-2])<=76:
    #         if len(diction['hcl'])==7 and diction['hcl'].startswith('#') and r.match(diction['hcl'][1:]):
    #             if diction['ecl'] in ['amb', 'blu', 'brn',' gry',' grn' ,'hzl',' oth']:
    #                 if len(diction['pid'])==9 and diction['pid'].isnumeric():
    #                     counter+=1
    #                     res.append(valid)

    if 1920 <= int(diction['byr']) <= 2002 and len(diction['byr']) == 4 and diction['byr'].isnumeric():
        if 2010 <= int(diction['iyr']) <= 2020 and len(diction['iyr']) == 4 and diction['iyr'].isnumeric():
            if 2020 <= int(diction['eyr']) <= 2030 and len(diction['eyr']) == 4 and diction['eyr'].isnumeric():
                if diction['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    if len(diction['pid']) == 9 and diction['pid'].isnumeric():
                        if diction['hgt'].endswith('cm') or diction['hgt'].endswith('in'):
                            if diction['hgt'].endswith('cm'):
                                if 150 <= int(diction['hgt'][:len(diction['hgt']) - 2]) <= 193:
                                    if len(diction['hcl']) == 7 and diction['hcl'].startswith('#') and diction['hcl'][1:].isalnum():
                                        for letter in diction['hcl'][1:]:
                                            if letter in 'ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                                                break
                                        RESS += 1
                                        res.append(valid)
                            elif diction['hgt'].endswith('in'):
                                if 59 <= int(diction['hgt'][:len(diction['hgt']) - 2]) <= 76:
                                    if len(diction['hcl']) == 7 and diction['hcl'].startswith('#') and diction['hcl'][1:].isalnum():
                                        for letter in diction['hcl'][1:]:
                                            if letter in 'ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                                                break
                                        RESS += 1
                                        res.append(valid)
print(RESS)
print(res)
