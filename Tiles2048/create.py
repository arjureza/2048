'''
    Used to create a new 2048 board with 2 '2' tiles at random places
    
    Baselined: 3/12/2021
    
    Modified: 3/12/2021
    
    @author: Arju Reza
'''
from random import randint
import hashlib

def _create(userParms):
    # creates empty dictionary
    result = dict()
    
    # creates a new grid and adds it to the dictionary
    # https://stackoverflow.com/questions/7595106/python-inserting-characters-between-other-characters-at-random-points
    grid = '00000000000000'
    for _ in range(2):
        pos = randint(0, len(grid) - 1)
        grid = "".join((grid[:pos], '2', grid[pos:]))
    result['grid'] = grid
    
    # creates a score dictionary key and value and initializes it to 0
    score = '0'
    result['score'] = score
    
    # concatenates grid and score together, encodes it using sha-256, and adds it to the dictionary
    # used code given by Dr. Umphress in Assignment 4 page
    gridStr = result['grid']
    scoreStr = result['score']
    integrityStr = gridStr + "." + scoreStr
    my_hash = hashlib.sha256()
    my_hash.update(integrityStr.encode())
    enc_integrity = my_hash.hexdigest()
    enc_upper_integrity = enc_integrity.upper()
    result['integrity'] = enc_upper_integrity
    
    # creates a status dictionary key and value and sets it to 'ok' (for now)
    status = 'ok'
    result['status'] = status
    
    return result
    