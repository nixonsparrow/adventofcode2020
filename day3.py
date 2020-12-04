from day3i import day3

test_input = r'''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''


def clean_input(some_input):
    input_to_return = []
    for row in some_input.split('\n'):
        input_to_return.append(row)
    return input_to_return


def check_if_tree(y, x):
    while x >= len(y):
        x -= len(y)

    return True if y[x] == '#' else False


def navigation(some_input, coordinates=(3, 1)):
    position, trees, row = 0, 0, 0
    rows = clean_input(some_input)

    while row < len(rows):

        if check_if_tree(rows[row], position):
            trees += 1

        position += coordinates[0]
        row += coordinates[1]

    print('Trees:', trees)
    return trees


def multiply_navigation(the_input, coordinates_list):
    trees_list = []
    #
    for coordinates in coordinates_list:
        trees_list.append(navigation(the_input, coordinates))

    x = 0
    for y in trees_list:
        if not x:
            x = y
        else:
            x *= y

    return x


if __name__ == '__main__':
    print('All trees:', multiply_navigation(day3, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
