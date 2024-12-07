import time
start = time.time()

with open('day4.txt') as f:
    data = f.read().split('\n\n')

def parse_passports(data):
    passports = []
    for passport in data:
        passport = ' '.join(passport.split('\n'))
        passport = dict([kv.split(':') for kv in passport.split(' ')])
        passports.append(passport)
    return passports

passports = parse_passports(data)
part1keys = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
print(sum([part1keys == set(passport.keys()).intersection(part1keys) for passport in passports]))
    
def part2(passports):
    valid = 0
    for passport in passports:
        if not part1keys == set(passport.keys()).intersection(part1keys):
            continue
        if not 1920 <= int(passport['byr']) <= 2002:
            continue
        if not 2010 <= int(passport['iyr']) <= 2020:
            continue
        if not 2020 <= int(passport['eyr']) <= 2030:
            continue
        hgt_unit = passport['hgt'][-2:]
        if not hgt_unit in ['cm','in']:
            continue
        if hgt_unit == 'cm' and not (150 <= int(passport['hgt'][:-2]) <= 193):
            continue
        if hgt_unit == 'in' and not (59 <= int(passport['hgt'][:-2]) <= 76):
            continue
        if not passport['hcl'][0] == '#':
            continue
        hcl = set(passport['hcl'][1:])
        hex = set('0123456789abcdef')
        if not len(hcl) == len(hcl.intersection(hex)):
            # print(passport['hcl'])
            continue
        if not passport['ecl'] in 'amb blu brn gry grn hzl oth'.split():
            # print(passport['ecl'])
            continue
        if not 9 == len(passport['pid']):
            # print(passport['pid'])
            continue
        # print(passport)
        valid += 1
    return valid

print(part2(passports))

print('time taken', time.time()-start, 'secs')