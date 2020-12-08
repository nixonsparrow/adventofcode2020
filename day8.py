from day8i import day8
from itertools import *
from copy import deepcopy

test_input = r'''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def clean_input(some_input):
    input_to_return = []
    for row in some_input.split('\n'):
        x = row.split()
        input_to_return.append(x)
    return input_to_return


def boot_operator(code):
    i = 0
    indexes_list = []
    accumulator_value = 0
    while True:
        if i in indexes_list:
            return accumulator_value, True
        else:
            indexes_list.append(i)

        try:
            if code[i][0] == 'acc':
                accumulator_value += int(code[i][1])
                i += 1
            elif code[i][0] == 'jmp':
                i += int(code[i][1])
            else:
                i += 1
        except IndexError:
            if i >= len(code):
                return accumulator_value, False
            else:
                return None, True


def to_loop_or_not_to_loop(instructions):
    accumulator_value = 0
    found = False

    while not found:
        for x in range(0, len(instructions)):
            instruction = instructions[x]
            changed_instructions = deepcopy(instructions)
            if instruction[0] == 'acc':
                continue
            else:

                if instruction[0] == 'jmp':
                    changed_instructions[x][0] = 'nop'
                else:
                    changed_instructions[x][0] = 'jmp'

                accumulator_value, is_loop = boot_operator(changed_instructions)

                if not is_loop:
                    found = True
                    break

    return accumulator_value


if __name__ == '__main__':
    print('Result:', to_loop_or_not_to_loop(clean_input(day8)))
