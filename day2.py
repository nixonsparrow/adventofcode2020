from day2i import day2
from itertools import *

test_input = r'''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''


def clean_input(some_input):
    input_to_return = []
    for row in some_input.split('\n'):
        row_splitted = row.split()
        input_to_return.append({'letter': row_splitted[1][0], 'min': int(row_splitted[0].split('-')[0]), 'max': int(row_splitted[0].split('-')[-1]), 'password': row_splitted[-1]})
        # print(input_to_return)
    return input_to_return


def check_passwords(passwords):
    i = 0
    for password in passwords:
        if password['max'] >= password['password'].count(password['letter']) >= password['min']:
            # print(password, 'OK')
            i += 1
        else:
            # print(password, 'NOT!')
            pass
    return i


def check_passwords_part2(passwords):
    i = 0
    for password in passwords:
        a = password['letter'] == password['password'][password['max']-1]
        b = password['letter'] == password['password'][password['min']-1]
        if a and not b or b and not a:
            i += 1

    return i


if __name__ == '__main__':
    print(check_passwords_part2(clean_input(day2)))
