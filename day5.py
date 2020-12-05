from day5i import day5
from itertools import *

test_input = r'''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''


def clean_input(some_input):
    input_to_return = []
    for row in some_input.split('\n'):
        input_to_return.append(row)
    return input_to_return


def read_all_seats(all_seats, first_part=True):
    highest_id = 0
    arrangement = {}
    for seat in all_seats:
        seat_id, seat_row_col = read_seat(seat)
        highest_id = seat_id if seat_id > highest_id else highest_id

        if not first_part:
            arrangement[seat_row_col] = 'X'

    if first_part:
        return highest_id, len(all_seats)

    # print whole plane and gather all seats
    for row in range(0, 127):

        if len(str(row)) == 1:
            col_to_print = f'00{row} '
        elif len(str(row)) == 2:
            col_to_print = f'0{row} '
        else:
            col_to_print = f'{row} '

        for col in range(0, 7):
            if (row, col) not in arrangement:
                arrangement[(row, col)] = ' '
            col_to_print += arrangement[(row, col)]
        print(col_to_print)

    # find your seat
    for seat in arrangement:
        if arrangement[seat] == ' ':
            right_neighbour, left_neighbour = (seat[0], seat[1] + 1), (seat[0], seat[1] - 1)
            if right_neighbour in arrangement and left_neighbour in arrangement:
                if arrangement[left_neighbour] == 'X' and arrangement[right_neighbour] == 'X':

                    return get_seat_id(seat)


def get_seat_id(row_col):
    row, col = row_col
    return row * 8 + col


def read_seat(seat):
    rows_range = [0, 127]
    for x in seat[0:7]:
        x_range = range(rows_range[0], rows_range[1])
        mid_row = int(sum(x_range)/len(x_range))
        # print(seat, x, mid_row)
        if x == 'B':
            rows_range[0] = mid_row + 1
        else:
            rows_range[1] = mid_row

    col_range = [0, 8]
    for y in seat[7:]:
        y_range = range(col_range[0], col_range[1])
        corridor = int(sum(y_range)/len(y_range))
        # print(seat, y)
        if y == 'R':
            col_range[0] = corridor + 1
        else:
            col_range[1] = corridor

    seat_id = get_seat_id((rows_range[0], col_range[0]))

    return seat_id, (rows_range[0], col_range[0])


if __name__ == '__main__':
    print(read_all_seats(clean_input(day5), first_part=False))
    # print(read_seat(clean_input(test_input)[0]))
