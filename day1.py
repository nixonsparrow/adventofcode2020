from day1i import day1
from itertools import *

test_input = r'''1721
979
366
299
675
1456'''


def clear_input(x_list):
    to_return = []
    for x in x_list.split('\n'):
        to_return.append(int(x))
    return to_return


def get_combinations(some_list):
    return combinations(clear_input(some_list), 3)


def main(some_input):
    for x in get_combinations(some_input):
        print(x)
        if sum(x) == 2020:
            print('SCORE')
            return x[0] * x[1] * x[2]


if __name__ == '__main__':
    print(main(day1))
