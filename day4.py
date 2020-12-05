import csv
import re

def validation(key, val):
    if key == 'byr':
        return (int(val) >= 1920 and int(val) <= 2002)
    elif key == 'iyr':
        return (int(val) >= 2010 and int(val) <= 2020)
    elif key == 'eyr':
        return (int(val) >= 2020 and int(val) <= 2030)
    elif key == 'hgt':
        if val[-2:] == 'cm':
            return (int(val[:-2]) >= 150 and int(val[:-2]) <= 193)
        if val[-2:] == 'in':
            return (int(val[:-2]) >= 59 and int(val[:-2]) <= 76)
    elif key == 'hcl':
        pattern = re.compile(r'^#[\da-f]{6}')
        return pattern.match(val)
    elif key == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        pattern = re.compile(r'^[\d]{9}$')
        return pattern.match(val)
    else:
        return False
    

def challenge1(input):
    passport_ct=0
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    all_passports, accum = [], []
    for line in input:
        if len(line) != 0:
            accum += line
        else:
            all_passports += [' '.join(accum)]
            accum = []
    all_passports += [' '.join(accum)]

    for passport in all_passports:
        fields = passport.split(' ')
        check = set()
        for field in fields:
            key, val = field.split(':')[0], field.split(':')[1]
            if key != 'cid' and key != '':
                if validation(key, val):
                    check.add(key)
        if req_fields == check:
            passport_ct+=1

    return passport_ct

if __name__ == '__main__':
    with open('inputs/day4_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    with open('inputs/day4_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    print(challenge1(input))

    