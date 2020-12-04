import fileinput
import string

passes = []
passport = {}
for line in fileinput.input():
    if line == '\n':
        passes.append(passport)
        passport = {}
    else:
        for keyval in line.split():
            key, val = keyval.split(':')
            passport[key] = val
passes.append(passport)

fields = {'byr', 'iyr', 'eyr','hgt', 'hcl', 'ecl', 'pid'}
valid = 0

for passport in passes:
    if all(field in passport for field in fields):
        if len(passport['byr']) != 4 or not (1920 <= int(passport['byr']) <= 2002):
            continue 
        if len(passport['iyr']) != 4 or not (2010 <= int(passport['iyr']) <= 2020):
            continue 
        if len(passport['eyr']) != 4 or not (2020 <= int(passport['eyr']) <= 2030):
            continue 
        
        if passport['hgt'].endswith('cm'):
            h = passport['hgt'][:passport['hgt'].index('cm')]
            if len(h) != 3 or not (150 <= int(h) <= 193):
                continue
        elif passport['hgt'].endswith('in'):
            h = passport['hgt'][:passport['hgt'].index('in')]
            if len(h) != 2 or not (59 <= int(h) <= 76):
                continue
        else:
            continue
        
        if not passport['hcl'].startswith('#') or any(c not in string.hexdigits for c in passport['hcl'][1:]):
            continue
        if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            continue
        if len(passport['pid']) != 9 or any(not c.isdigit() for c in passport['pid']):
            continue
        valid += 1
print(passport.keys())
print(valid)