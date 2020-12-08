from day8i import day8
from itertools import *
from copy import deepcopy
import time

test_input = r'''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def clean_input(some_input):  # returns input as list of lists (each contains [command, value])
    input_to_return = []
    for row in some_input.split('\n'):
        row_as_list = row.split()
        row_as_list[1] = int(row_as_list[1])
        input_to_return.append(row_as_list)
    return input_to_return


def boot_operator(instructions):  # returns (achieved accumulator value or None, True if loop else False)
    i = 0
    indexes_list = []
    accumulator_value = 0
    while True:
        if i in indexes_list:
            return accumulator_value, True
        else:
            indexes_list.append(i)

        try:
            current_command, current_value = instructions[i]
            if current_command == 'acc':
                accumulator_value += current_value
                i += 1
            elif current_command == 'jmp':
                i += current_value
            else:
                i += 1
        except IndexError:
            if i == len(instructions):
                return accumulator_value, False
            else:
                return None, True


def to_loop_or_not_to_loop(instructions):  # searches for first possible instructions with one changed jmp <=> nop
    accumulator_value = 0                  # exactly one is changed during every try
    found = False

    while not found:
        for number in range(0, len(instructions)):
            command, value = instructions[number]
            if command == 'acc':
                continue
            else:

                if command == 'jmp':  # change 'number' indexed value, try it, change value back to before
                    instructions[number][0] = 'nop'
                    accumulator_value, is_loop = boot_operator(instructions)
                    instructions[number][0] = 'jmp'
                else:
                    instructions[number][0] = 'jmp'
                    accumulator_value, is_loop = boot_operator(instructions)
                    instructions[number][0] = 'nop'

                if not is_loop:
                    found = True
                    break

    return accumulator_value


if __name__ == '__main__':
    start = time.time()
    print('Result:', to_loop_or_not_to_loop(clean_input(day8)))  # part 2 result
    print('Time:', time.time()-start)
