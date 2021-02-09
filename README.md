# Skyscrapers

This module is created for a game "Skycrapers".
With the help of this module you can check game board to know whether board is ready for game,
whether all placements of scyscrapers correspond to the rules of game.

This module consists of following functions:

def read_input(path) - to read the current state of the board from the file

def delete_stars(row) - to delete stars from row

def left_to_write_check(input_line, pivot) - check row-wise visibility from left to right

def check_not_finished_board(board) - check if skyscraper board is not finished, i.e., '?' present on the game board

def check_uniqueness_in_rows(board) - check buildings of unique height in each row

def check_horizontal_visibility(board) - check row-wise visibility (left-right and vice versa)

def check_columns(board) -  check column-wise compliance of the board for uniqueness

(buildings of unique height) and visibility (top-bottom and vice versa)

def check_skyscrapers(input_path) - main function to check the status of skyscraper game board
