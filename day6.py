from day6i import day6
from itertools import *

test_input = r'''abc

a
b
c

ab
ac

a
a
a
a

b'''


def clean_input(some_input, second=False):
    input_to_return = []

    if second:
        current_group, answers, people = {}, '', 0
        i = 0
        for row in some_input.split('\n'):
            if row == '':
                current_group['id'], current_group['answers'], current_group['people'] = i, answers, people
                i += 1
                input_to_return.append(current_group)
                current_group, answers, people = {}, '', 0
                continue
            else:
                answers += row
                people += 1

        current_group['id'], current_group['answers'], current_group['people'] = i, answers, people
        i += 1
        input_to_return.append(current_group)

    else:
        current_group = ''
        for row in some_input.split('\n'):
            if row == '':
                input_to_return.append(current_group)
                current_group = ''
                continue
            else:
                current_group += row

        input_to_return.append(current_group)

    return input_to_return


def part2(some_input):
    groups = clean_input(some_input, second=True)
    part2_sum = 0
    for group in groups:
        letters_correct = ''
        for letter in group['answers']:
            if letter in letters_correct:
                continue
            if group['people'] == group['answers'].count(letter):
                letters_correct += letter
                part2_sum += 1

    return part2_sum


def part1(some_input):
    groups = clean_input(some_input)
    current_set = ''
    part1_count = 0
    for group in groups:
        for letter in group:
            if letter not in current_set:
                current_set += letter

        part1_count += len(current_set)
        current_set = ''

    return part1_count


if __name__ == '__main__':
    print('Part 1:', part1(day6))
    print('Part 2:', part2(day6))
