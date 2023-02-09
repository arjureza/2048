import unittest
import Tiles2048.shift as shift
import hashlib
from Tiles2048.shift import _string_to_grid

class ShiftTest(unittest.TestCase):
#     def test_010_CorrectImplementationTest(self):
#         userParms = {'op': 'shift', 'grid': '2222444488881616160', 'score': '9600', 'direction': 'up',
#                       'integrity': '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'}
#         result = shift._shift(userParms)
#         
#         expected_grid = '2222444488881616164'
#         grid = result['grid']
#         self.assertEqual(grid, expected_grid)
#         
#         expected_score = '9600'
#         score = result['score']
#         self.assertEqual(score, expected_score)
#         
#         expected_status = 'lose'
#         status = result['status']
#         self.assertEqual(status, expected_status)
#         
#     
#     def test_020_ErrorTestingNoEmptyTiles(self):
#         userParms = {'op': 'shift', 'grid': '2222222222222222', 'score': '32', 
#                      'direction': 'down', 'integrity': '956644B1B6F313E39597D9F7EF748313D36646553D25AC48693335ED1808290C'}
#         actual_result = shift._shift(userParms)
#         
#         error_value = actual_result['status']
#         error_expected = 'error: no shift possible'
#         self.assertEqual(error_value, error_expected)
#         
#     def test_030_GridToStringAndStringToGridTest(self):   
#         string = '2020202020202020'    
#         grid_string_expected = string
#         grid_expected = [[2, 0, 2, 0], [2, 0, 2, 0], [2, 0, 2, 0], [2, 0, 2, 0]]
#         
#         grid = shift._string_to_grid(string)
#         
#         grid_string = shift._grid_to_string(grid_expected)
#         
#         self.assertEqual(grid_expected, grid)
#         self.assertEqual(grid_string_expected, grid_string)
#         
#     def test_040_GridErrorTest(self):
#         userParms = {'op': 'shift', 'grid': 1, 'score': '32', 
#                      'direction': 'down', 'integrity': '956644B1B6F313E39597D9F7EF748313D36646553D25AC48693335ED1808290C'}
#         actual_result = shift._shift(userParms)
#         
#         error_value = actual_result['status']
#         error_expected = 'error: invalid grid'
#         self.assertEqual(error_value, error_expected)
#         
#     def test_050_ScoreErrorTest(self):
#         userParms = {'op': 'shift', 'grid': '2020202020202020', 'score': '-20', 
#                      'direction': 'down', 'integrity': '956644B1B6F313E39597D9F7EF748313D36646553D25AC48693335ED1808290C'}
#         actual_result = shift._shift(userParms)
#         
#         error_value = actual_result['status']
#         error_expected = 'error: invalid score'
#         self.assertEqual(error_value, error_expected)
#         
#     def test_060_DirectionErrorTest(self):
#         userParms = {'op': 'shift', 'grid': '2020202020202020', 'score': '32', 
#                      'direction': 'empty', 'integrity': '956644B1B6F313E39597D9F7EF748313D36646553D25AC48693335ED1808290C'}
#         actual_result = shift._shift(userParms)
#         
#         error_value = actual_result['status']
#         error_expected = 'error: invalid direction'
#         self.assertEqual(error_value, error_expected)
#         
#     def test_070_IntegrityErrorTest(self):
#         userParms = {'op': 'shift', 'grid': '2020202020202020', 'score': '32', 
#                      'direction': 'down', 'integrity': 2}
#         actual_result = shift._shift(userParms)
#         
#         error_value = actual_result['status']
#         error_expected = 'error: invalid integrity'
#         self.assertEqual(error_value, error_expected)
# 
#     
#     def test_090_CorrectStatusTest(self):
#         grid = [[2, 0, 2, 0], [2, 0, 2, 0], [2, 0, 2, 0], [2, 0, 2, 0]]
#         expected_status = 'ok'
#         status = shift._find_status(grid)
#         self.assertEqual(status, expected_status)
#         
#         grid = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
#         expected_status = 'lose'
#         status = shift._find_status(grid)
#         self.assertEqual(status, expected_status)
#         
#         grid = [[2, 2, 2, 2], [2048, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 0]]
#         expected_status = 'win'
#         status = shift._find_status(grid)
#         self.assertEqual(status, expected_status)
#         
#     def test_090_CorrectShiftUp(self):
#         score = 0
#         grid = [[0, 0, 0, 0], [0, 0, 4, 0], [2, 4, 4, 0], [2, 0, 2, 0]]
#         expected_grid = [[4, 4, 8, 0], [0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#         
#         grid_score_array = shift._shift_up(grid, score)
#         grid = grid_score_array[0]
#         
#         self.assertEqual(grid, expected_grid)
#         
#         grid = [[0, 2, 4, 0], [2, 2, 2, 0], [0, 4, 2, 0], [0, 0, 0, 0]]
#         expected_grid = [[2, 4, 4, 0], [0, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#         
#         grid_score_array = shift._shift_up(grid, score)
#         grid = grid_score_array[0]
#         
#         self.assertEqual(grid, expected_grid)
#         
#     def test_100_CorrectShiftDown(self):
#         score = 0
#         grid = [[0, 0, 0, 0], [0, 0, 4, 0], [2, 4, 4, 0], [2, 0, 2, 0]]
#         expected_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 8, 0], [4, 4, 2, 0]]
#         
#         grid_score_array = shift._shift_down(grid, score)
#         grid = grid_score_array[0]
#         
#         self.assertEqual(grid, expected_grid)
#     
    def test_110_CorrectShiftLeft(self):
        grid_string = '2000000000002222'
        direction = ''
        score = '128'
        integ = shift._find_integrity(grid_string, score)
            
        userParms = dict()
            
        userParms['grid'] = grid_string
        userParms['direction'] = direction
        userParms['score'] = score
        userParms['integrity'] = integ
            
        result = shift._shift(userParms)
#            
#         print(result)
#           
#         
#     def test_120_CorrectShiftRight(self):
#         score = 0
#         grid = [[2, 0, 2, 2], [8, 0, 8, 0], [0, 0, 2, 2], [4, 0, 2, 2]]
#         expected_grid = [[0, 0, 2, 4], [0, 0, 0, 16], [0, 0, 0, 4], [0, 0, 4, 4]]
#         
#         grid_score_array = shift._shift_right(grid, score)
#         grid = grid_score_array[0]
#         
#         print(grid_score_array[1])
#         
#         self.assertEqual(grid, expected_grid)   
#         
#     def test_130_AddingNumberToGrid(self):
#         score = 0
#         grid = [[0, 2, 0, 2], [0, 2, 0, 2], [0, 2, 0, 2], [0, 2, 0, 2]]
#         
#         grid = shift._add_number_to_grid(grid)
#         print(grid)

    def test_140_CorrectLoseStatus(self):
        grid_string = '2481632641282562481632641280'
        direction = 'down'
        score = '9600'
        integ = shift._find_integrity(grid_string, score)
            
        userParms = dict()
            
        userParms['grid'] = grid_string
        userParms['direction'] = direction
        userParms['score'] = score
        userParms['integrity'] = integ
            
        result = shift._shift(userParms)
          
        self.assertEqual(result['status'], 'lose')
        
    def test_150_CorrectOkStatus(self):
        grid_string = '2222444488881616160'
        direction = 'up'
        score = '9600'
        integ = shift._find_integrity(grid_string, score)
           
        userParms = dict()
           
        userParms['grid'] = grid_string
        userParms['direction'] = direction
        userParms['score'] = score
        userParms['integrity'] = integ
           
        result = shift._shift(userParms)
         
        self.assertEqual(result['status'], 'ok')
        
    def test_160_CorrectWinStatus(self):
        grid_string = '1024102400000000000000'
        direction = 'left'
        score = '129024'
        integ = shift._find_integrity(grid_string, score)
            
        userParms = dict()
            
        userParms['grid'] = grid_string
        userParms['direction'] = direction
        userParms['score'] = score
        userParms['integrity'] = integ
            
        result = shift._shift(userParms)
            
          
        self.assertEqual(result['status'], 'win')
    
    def test_170_Correct(self):
        grid_string = '0020000020000000'
        direction = ''
        score = '0'
        integ = shift._find_integrity(grid_string, score)
            
        userParms = dict()
            
        userParms['grid'] = grid_string
        userParms['direction'] = direction
        userParms['score'] = score
        userParms['integrity'] = integ
            
        result = shift._shift(userParms)
    
    def test_180_Correct(self):
        grid_string = '0000004024402020'
        direction = 'left'
        score = '4'
        integ = shift._find_integrity(grid_string, score)
            
        userParms = dict()
            
        userParms['grid'] = grid_string
        userParms['score'] = score
        userParms['integrity'] = integ
            
        result = shift._shift(userParms)
          
    
    
        