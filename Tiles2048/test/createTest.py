import unittest
import Tiles2048.create as create
import hashlib

class CreateTest(unittest.TestCase):
        
#     Create function testing
#     Happy path: 
#        1: Normal input of op = create
#            returns dictionary with values of:
#                grid with 2 '2' tiles at random places
#                score initially set at 0
#                integrity with a hash hexdigest of grid key concatenated with a period and score key
    def test_010_HappyPathNormalValues(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
         
        gridValue = actualResult['grid']
        numof2s = gridValue.count('2')
        self.assertEqual(2, numof2s)
         
        scoreValue = actualResult['score']
        self.assertEqual('0', scoreValue)
         
        integrityValue = actualResult['integrity']
        self.assertIsInstance(integrityValue, str)
         
        statusValue = actualResult['status']
        self.assertEqual('ok', statusValue)
        
    def test_050_GridTest(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        gridValue = actualResult['grid']
        print(gridValue)
        numof2s = gridValue.count('2')
        self.assertEqual(2, numof2s)
    
    def test_051_ScoreTest(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        scoreValue = actualResult['score']
        self.assertEqual('0', scoreValue)
        
    def test_052_IntegrityTest(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        integrityValue = actualResult['integrity']
        print(integrityValue)
        self.assertIsInstance(integrityValue, str)
        
    def test_052_StatusTest(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        statusValue = actualResult['status']
        expectedResult = 'ok'
        self.assertEqual(expectedResult, statusValue)
        
        
        
        
        