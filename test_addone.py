import pandas as pd
import unittest
import os
import sys

# To access jootang (in the parent repository)
parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from jootang.with_without.addone import addone

# Create a test class
class TestAddone(unittest.TestCase): 
    
    @classmethod
    def setUpClass(cls):
        print("Instantiating TestAddone object")
    
    def setUp(self):
        
        df1 = pd.read_csv("data/stackloss.csv", index_col = 0)        
        self.data1 = df1._get_numeric_data()
        self.response1 = 'stack.loss'
        self.nbuckets1 = 5
        self.output1 = [7.81, 9.6, 12.51, 19.56, 21.18]
                
        
        df2 = pd.read_csv("data/life_cycle_savings.csv", index_col = 0)
        self.data2 = df2._get_numeric_data()
        self.response2 = 'sr'
        self.nbuckets2 = 6
        self.output2 = [9.04, 6.61, 10.04, 11.56, 8.19]
        
        
        df3 = pd.read_csv("data/lawyer_ratings.csv", index_col = 0)
        self.data3 = df3._get_numeric_data()
        self.response3 = 'RTEN'
        self.nbuckets3 = 5
        self.output3 = [5.23, 5.91, 6.23, 7.46, 8.39]
        
        
        df4 = pd.read_csv("data/fish.csv", index_col = 0)
        self.data4 = df4._get_numeric_data()
        self.response4 = 'length'
        self.nbuckets4 = 4       
        self.output4 = [3107.43, 3107.43, 3107.43, 3107.43]
    
    
        df5 = pd.read_csv("data/weather.csv", index_col = 0)
        self.data5 = df5._get_numeric_data()
        self.response5 = 'Temperature..C.'
        self.nbuckets5 = 10       
        self.output5 = [1.98, 1.83, 14.77, 9.12, 14.05, 3.4, 4.7, 5.69, 7.41, 15.59]
        

    def test_addone(self):
        
        self.assertEqual(addone(self.data1, response = self.response1, nbuckets = self.nbuckets1), self.output1)
        self.assertEqual(addone(self.data2, response = self.response2, nbuckets = self.nbuckets2), self.output2)
        self.assertEqual(addone(self.data3, response = self.response3, nbuckets = self.nbuckets3), self.output3)
        self.assertEqual(addone(self.data4, response = self.response4, nbuckets = self.nbuckets4), self.output4)
        self.assertEqual(addone(self.data5, response = self.response5, nbuckets = self.nbuckets5), self.output5)

        
    def tearDown(self):
        print("Finished testing the test case.")

        
    @classmethod
    def tearDownClass(cls):
        print("Destroying TestAddone object")
