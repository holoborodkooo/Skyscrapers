"""
tut maje buty posylannia
"""
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    lst = []
    opened = open(path, 'r', encoding='utf-8')
    for line in opened.readlines():
        to_append = line[0:-1]
        lst.append(to_append)
    return lst


def delete_stars(row):
    """
    This function deletes stars from the row.
    >>> delete_stars('*1234**')
    '1234'
    """
    if '*' in row:
        while '*' in row:
            row = row.replace('*', '')
    return str(row)


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = delete_stars(input_line)
    visible_skyscrapers = 0
    maximus = 0
    for i in range(1, len(input_line)):
        if maximus < int(input_line[i]):
            maximus = int(input_line[i])
            visible_skyscrapers += 1
    return visible_skyscrapers == pivot


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
    '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = True
    for row in board:
        if '?' in row:
            result = False
            break
    return result


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if row[0] != '*':
            row_1 = delete_stars(row)
            for element in row_1[1:]:
                if row_1[1:].count(element) >  1:
                    return False
        if row[-1] != '*':
            row_1 = delete_stars(row)
            for element in row_1[:-1]:
                if row_1[:-1].count(element) >  1:
                    return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = True
    for row in board:
        if row[0] != '*':
            if left_to_right_check(row, int(row[0])) is False:
                return False
        if row[-1] != '*':
            lst = list(reversed(delete_stars(row)))
            reversed_row_str = ''
            for i in lst:
                reversed_row_str += i
            if left_to_right_check(reversed_row_str, int(lst[0])) is False:
                return False
    return result


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness\
    (buildings of unique height) and visibility (top-bottom and vice versa).
    Same as for horizontal cases, but aggregated in one function for\
    vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
    '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for i in range(0, len(board)):
        new_row = ''
        for row in board:
            new_row += row[i]
        new_board.append(new_row)
    for i in range(1, len(new_board)):
        for j in new_board[i]:
            if j != '*':
                if new_board[i][1:-1].count(j) > 1 :
                    return False
    return check_horizontal_visibility(new_board)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    if check_not_finished_board(board) is False:
        return False
    if check_horizontal_visibility(board) is False:
        return False
    if check_columns(board) is False:
        return False
    return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
