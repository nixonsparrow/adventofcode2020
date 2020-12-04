from day4i import day4
from itertools import *

test_input = r'''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''


def clean_input(some_input):
    input_to_return = []
    x = {}
    for row in some_input.split('\n'):
        for y in row.split(' '):
            try:
                x[y.split(':')[0]] = y.split(':')[1]
            except IndexError:
                pass

        if row == '' or some_input.split('\n').index(row) == len(some_input.split('\n')) - 1:
            input_to_return.append(x)
            x = {}
            continue

    return input_to_return


def document_reader(documents):
    documents_valid = []
    valid = 0
    for document in documents:
        if 'byr' not in document or 'iyr' not in document or 'eyr' not in document or 'hgt' not in document or 'hcl' not in document or 'ecl' not in document or 'pid' not in document:
            continue
        if not 1920 <= int(document['byr']) <= 2002:
            continue
        if not 2010 <= int(document['iyr']) <= 2020:
            continue
        if not 2020 <= int(document['eyr']) <= 2030:
            continue
        try:
            if document['hgt'][-2:] == 'in' and 59 <= int(document['hgt'][0:2]) <= 76 or document['hgt'][-2:] == 'cm' and 150 <= int(document['hgt'][0:3]) <= 193:
                pass
            else:
                continue
        except ValueError:
            continue
        if document['hcl'][0] == '#':
            not_valid = False
            for x in document['hcl'][1:]:
                if x not in '0123456789abcdef':
                    not_valid = True
                    break
            if not_valid:
                continue
        else:
            continue
        if document['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if len(document['pid']) == 9:
            not_valid = False
            for x in document['pid']:
                try:
                    temp = int(x)
                except ValueError:
                    not_valid = True
                    continue
            if not_valid:
                continue
        else:
            continue

        # print('VALID')
        valid += 1
        documents_valid.append(document)

    return valid, documents_valid


if __name__ == '__main__':
    print('BYR')
    for x in document_reader(clean_input(day4))[1]:
        print(x['byr'])
    print('IYR')
    for x in document_reader(clean_input(day4))[1]:
        print(x['iyr'])
    print('EYR')
    for x in document_reader(clean_input(day4))[1]:
        print(x['eyr'])
    print('HGT')
    for x in document_reader(clean_input(day4))[1]:
        print(x['hgt'])
    print('HCL')
    for x in document_reader(clean_input(day4))[1]:
        print(x['hcl'])
    print('ECL')
    for x in document_reader(clean_input(day4))[1]:
        print(x['ecl'])
    print('PID')
    for x in document_reader(clean_input(day4))[1]:
        print(x['pid'])
    print(document_reader(clean_input(day4))[0])