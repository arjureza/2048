'''
    Shifts the current state of the board in specified direction
    
    Baselined: 4/2/2021
    
    Modified: 4/28/2021
    
    @author: Arju Reza
'''

from math import log2
from random import choice
import hashlib

def _shift(userParms):
    # variables
    result = dict()
    
    if not('grid' in userParms):
        result['status'] = 'error: missing grid'
        return result
    grid_string = userParms['grid']
    score_string = userParms['score']
    
    # score error check
    if (score_string == '') or (score_string == None):
        result['status'] = 'error: empty score'
        return result
    if not(score_string.isdigit()):
        result['status'] = 'error: invalid score'
        return result
    score = int(score_string)
    if ((score % 2) == 1):
        result['status'] = 'error: invalid score'
        return result
    
    # if direction is empty, set it to down
    if not('direction' in userParms):
        userParms['direction'] = 'down'
    
    direction_string = userParms['direction']
    if (direction_string == ''):
        direction_string = 'down'
    
    integrity_string = userParms['integrity']
    
    # grid error check
    if (grid_string == ''):
        result['status'] = 'error: invalid grid'
        return result
    if not(isinstance(grid_string, str)):
        result['status'] = 'error: invalid grid'
        return result    
    
    # makes grid out of string for grid and checks if there are 16 tiles in it (if not return error)
    grid_num_of_tiles_array = _string_to_grid(grid_string)
    grid = grid_num_of_tiles_array[0]
    num_of_tiles = grid_num_of_tiles_array[1]
    if (num_of_tiles != 16):
        result['status'] = 'error: invalid grid'
        return result
    
    # error checking
    # no empty tiles error
#     no_empty_error = _empty_tile_check(grid)
#     if no_empty_error:
#         result['status'] = 'error: no shift possible' 
#         return result
    
    # faulty parameter error
    if not((isinstance(score_string, str)) and (score >= 0)):
        result['status'] = 'error: invalid score'
        return result
    elif (direction_string.upper() != 'UP') and (direction_string.upper() != 'DOWN') and (direction_string.upper() != 'LEFT') and (direction_string.upper() != 'RIGHT'):
        result['status'] = 'error: invalid direction'
        return result
    elif not((isinstance(integrity_string, str)) and (integrity_string != '')):
        result['status'] = 'error: invalid integrity'
        return result
    
    # check to see if integrity value is correct
    test_integrity_string = _find_integrity(grid_string, score_string)
    if (test_integrity_string != integrity_string):
        result['status'] = 'error: invalid integrity'
        return result
    
    # shift grid in specified direction
    if (direction_string.upper() == 'UP'):
        grid_score_list = _shift_up(grid, score)
        grid = grid_score_list[0]
        score = grid_score_list[1]
    elif (direction_string.upper() == 'DOWN'):
        grid_score_list = _shift_down(grid, score)
        grid = grid_score_list[0]
        score = grid_score_list[1]
    elif (direction_string.upper() == 'LEFT'):
        grid_score_list = _shift_left(grid, score)
        grid = grid_score_list[0]
        score = grid_score_list[1]
    else:
        grid_score_list = _shift_right(grid, score)
        grid = grid_score_list[0]
        score = grid_score_list[1]
    
    # inserts either 2 or 4 into empty space on grid
    grid = _add_number_to_grid(grid)
    
    # converts grid to string and add to result
    grid_string = _grid_to_string(grid)
    result['grid'] = grid_string
    
    # calculate the score of the grid
    score_string = str(score)
    result['score'] = score_string
    
    # creates and adds integrity key and value
    integrity_string = _find_integrity(grid_string, score_string)
    result['integrity'] = integrity_string
    
    # finds the status of the board
    final_grid_tiles = _string_to_grid_with_2048(grid_string)
    final_grid = final_grid_tiles[0]
    status_string = _find_status(final_grid)
    result['status'] = status_string
    
    return result

# check for empty tiles in grid
# https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/
def _empty_tile_check(grid):
    for row in range(0, 4):
        for column in range(0, 4):
            if (grid[row][column] == 0):
                return False
    return True

# makes a 4x4 grid using grid string from userParms
# https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two
# 
def _string_to_grid(grid_string):
    temp_string = ''
    row = 0
    column = 0
    num_of_tiles = 0
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  
    for i in range(len(grid_string)):
        temp_string += grid_string[i]
        temp_int = int(temp_string)
        if (temp_int == 0):
            grid[row][column] = temp_int
            num_of_tiles += 1;
            temp_string = ''
            column += 1
            if column == 4:
                column = 0
                row += 1        
        elif (temp_int > 1) and (log2(temp_int).is_integer()):
            if (i < len(grid_string) - 2) and (temp_int == 2):                
                if (grid_string[i+1] == '5') and (grid_string[i+2] == '6'):
                    continue
                else:                
                    grid[row][column] = temp_int
                    num_of_tiles += 1;
                    temp_string = ''
                    column += 1
                    if column == 4:
                        column = 0
                        row += 1
            else:                
                grid[row][column] = temp_int
                num_of_tiles += 1;
                temp_string = ''
                column += 1
                if column == 4:
                    column = 0
                    row += 1
                              
    return [grid, num_of_tiles]

# same as _string_to_grid expect it includes the possibility of 2048 in the grid
def _string_to_grid_with_2048(grid_string):
    temp_string = ''
    row = 0
    column = 0
    num_of_tiles = 0
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  
    for i in range(len(grid_string)):
        temp_string += grid_string[i]
        temp_int = int(temp_string)
        if (temp_int == 0):
            grid[row][column] = temp_int
            num_of_tiles += 1;
            temp_string = ''
            column += 1
            if column == 4:
                column = 0
                row += 1        
        elif (temp_int > 1) and (log2(temp_int).is_integer()):
            if (i < len(grid_string) - 3) and (temp_int == 2):
                if (grid_string[i+1] == '0') and (grid_string[i+2] == '4') and (grid_string[i+3] == '8'):
                    continue
            if (i < len(grid_string) - 2) and (temp_int == 2):                
                if (grid_string[i+1] == '5') and (grid_string[i+2] == '6'):
                    continue
                else:                
                    grid[row][column] = temp_int
                    num_of_tiles += 1;
                    temp_string = ''
                    column += 1
                    if column == 4:
                        column = 0
                        row += 1
            else:                
                grid[row][column] = temp_int
                num_of_tiles += 1;
                temp_string = ''
                column += 1
                if column == 4:
                    column = 0
                    row += 1
                              
    return [grid, num_of_tiles]
    
# makes grid back into string
def _grid_to_string(grid):
    a = ''
    for row in range(0, 4):
        for column in range(0, 4):
            element_string = (str(grid[row][column]))
            a += element_string
    return a

# shift up action on the grid    
def _shift_up(grid_input, score):
    grid = grid_input
    for _ in range(3):      
        for column in range(0, 4):
            for row in range(0, 3):
                if (grid[row][column] == 0):
                    grid[row][column] = grid[row + 1][column]
                    grid[row + 1][column] = 0
    for column in range(0, 4):
        for row in range(0, 3):
            if (grid[row][column] == grid[row + 1][column]):
                grid[row][column] *= 2
                score += grid[row][column]
                grid[row + 1][column] = 0
                for row in range(0, 3):
                    if (grid[row][column] == 0):
                        grid[row][column] = grid[row + 1][column]
                        grid[row + 1][column] = 0
            elif (grid[row][column] == 0):
                grid[row][column] = grid[row + 1][column]
                grid[row + 1][column] = 0
    return [grid, score]

# shift down action on the grid
def _shift_down(grid_input, score):
    grid = grid_input
    for _ in range(3):
        for column in range(0, 4):
            for row in range(3, 0, -1):
                if (grid[row][column] == 0):
                    grid[row][column] = grid[row - 1][column]
                    grid[row - 1][column] = 0
    for column in range(0, 4):
        for row in range(3, 0, -1):
            if (grid[row][column] == grid[row - 1][column]):
                grid[row][column] *= 2
                score += grid[row][column]
                grid[row - 1][column] = 0
                for row in range(3, 0, -1):
                    if (grid[row][column] == 0):
                        grid[row][column] = grid[row - 1][column]
                        grid[row - 1][column] = 0
            elif (grid[row][column] == 0):
                grid[row][column] = grid[row - 1][column]
                grid[row - 1][column] = 0
    return [grid, score]

# shift left action on the grid
def _shift_left(grid_input, score):
    grid = grid_input
    for _ in range(3):
        for row in range(0, 4):
            for column in range(0, 3):
                if (grid[row][column] == 0):
                    grid[row][column] = grid[row][column + 1]
                    grid[row][column + 1] = 0 
    for row in range(0, 4):
            for column in range(0, 3):
                if (grid[row][column] == grid[row][column + 1]):
                    grid[row][column] *= 2
                    score += grid[row][column]
                    grid[row][column + 1] = 0
                    for column in range(0, 3):
                        if (grid[row][column] == 0):
                            grid[row][column] = grid[row][column + 1]
                            grid[row][column + 1] = 0                          
                elif (grid[row][column] == 0):
                    grid[row][column] = grid[row][column + 1]
                    grid[row][column + 1] = 0
    return [grid, score]

# shift right action on the grid
def _shift_right(grid_input, score):
    grid = grid_input
    for _ in range(3):
        for row in range(0, 4):
            for column in range(3, 0, -1):
                if (grid[row][column] == 0):
                    grid[row][column] = grid[row][column - 1]
                    grid[row][column - 1] = 0
    for row in range(0, 4):
            for column in range(3, 0, -1):
                if (grid[row][column] == grid[row][column - 1]):
                    grid[row][column] *= 2
                    score += grid[row][column]
                    grid[row][column - 1] = 0
                    for column in range(3, 0, -1):
                        if (grid[row][column] == 0):
                            grid[row][column] = grid[row][column - 1]
                            grid[row][column - 1] = 0
                elif (grid[row][column] == 0):
                    grid[row][column] = grid[row][column - 1]
                    grid[row][column - 1] = 0
    return [grid, score]
            
# finds the integrity for the board           
def _find_integrity(grid_string, score_string):
    integrity_string = grid_string + "." + score_string
    my_hash = hashlib.sha256()
    my_hash.update(integrity_string.encode())
    enc_integrity = my_hash.hexdigest()
    enc_upper_integrity = enc_integrity.upper()
    return enc_upper_integrity

# finds the status of grid
def _find_status(grid):
    lose = False
    status = ''
    win = False
    filler_score = 0
    
    # checks to see if grid can be shifted, if cannot be shifted, set status to lose
    initial_grid_string = _grid_to_string(grid)
    shifted_grid_score = _shift_down(grid, filler_score)
    shifted_grid = shifted_grid_score[0]
    final_grid = _add_number_to_grid(shifted_grid)
    initial_grid = _string_to_grid_with_2048(initial_grid_string)[0]
    
    if (initial_grid == final_grid):
        shifted_grid_score = _shift_up(grid, filler_score)
        shifted_grid = shifted_grid_score[0]
        if (initial_grid == shifted_grid):
            shifted_grid_score = _shift_left(grid, filler_score)
            shifted_grid = shifted_grid_score[0]
            if (initial_grid == shifted_grid):
                shifted_grid_score = _shift_right(grid, filler_score)
                shifted_grid = shifted_grid_score[0]
                if (initial_grid == shifted_grid):
                    lose = True
    
    # checks for 2048 in grid and if yes, set status to win
    for row in range(0, 4):
        for column in range(0, 4):
            if (grid[row][column] == 2048):
                win = True
    
    if (win):
        status = 'win'
    elif (lose):
        status = 'lose'
    else:
        status = 'ok'
    return status 

def _add_number_to_grid(grid):
    # if there are no 0s in the list, return grid as is
    no_empty_tiles = _empty_tile_check(grid)
    if (no_empty_tiles):
        return grid
    
    row_column_indexes = list()
    for row in range(0, 4):
        for column in range(0, 4):
            if (grid[row][column] == 0):
                row_column_indexes.append([row, column])
    
    row_column_array = choice(row_column_indexes)
    
    number_to_insert = choice([2, 4])
    
    row = row_column_array[0]
    column = row_column_array[1]
    
    grid[row][column] = number_to_insert
    
    return grid
    
                
                
    