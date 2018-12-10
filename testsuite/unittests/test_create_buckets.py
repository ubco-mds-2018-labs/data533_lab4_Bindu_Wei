import pandas as pd
import unittest
import os
import sys

# To access jootang (in the parent repository)
parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from jootang.with_without.create_buckets import buckets

# Create a test class
class TestCreateBuckets(unittest.TestCase): 
    
    @classmethod
    def setUpClass(cls):
        print("Instantiating TestCreateBuckets object")
    
    def setUp(self): 
               
        self.output1 = ['[0, 4.83)',
                         '[0, 4.83)',
                         '[0, 4.83)',
                         '[0, 4.83)',
                         '[0, 4.83)',
                         '[4.83, 9.67)',
                         '[4.83, 9.67)',
                         '[4.83, 9.67)',
                         '[4.83, 9.67)',
                         '[4.83, 9.67)',
                         '[9.67, 14.5)',
                         '[9.67, 14.5)',
                         '[9.67, 14.5)',
                         '[9.67, 14.5)',
                         '[9.67, 14.5)',
                         '[14.5, 19.33)',
                         '[14.5, 19.33)',
                         '[14.5, 19.33)',
                         '[14.5, 19.33)',
                         '[14.5, 19.33)',
                         '[19.33, 24.17)',
                         '[19.33, 24.17)',
                         '[19.33, 24.17)',
                         '[19.33, 24.17)',
                         '[19.33, 24.17)',
                         '[24.17, 29]',
                         '[24.17, 29]',
                         '[24.17, 29]',
                         '[24.17, 29]',
                         '[24.17, 29]']

        
        self.output2 = ['[0, 3.17)',
                         '[0, 3.17)',
                         '[0, 3.17)',
                         '[0, 3.17)',
                         '[3.17, 6.33)',
                         '[3.17, 6.33)',
                         '[3.17, 6.33)',
                         '[6.33, 9.5)',
                         '[6.33, 9.5)',
                         '[6.33, 9.5)',
                         '[9.5, 12.67)',
                         '[9.5, 12.67)',
                         '[9.5, 12.67)',
                         '[12.67, 15.83)',
                         '[12.67, 15.83)',
                         '[12.67, 15.83)',
                         '[15.83, 19]',
                         '[15.83, 19]',
                         '[15.83, 19]',
                         '[15.83, 19]']
        
        self.output3 = ['[0, 1.5)',
                         '[0, 1.5)',
                         '[1.5, 3.0)',
                         '[3.0, 4.5)',
                         '[3.0, 4.5)',
                         '[4.5, 6.0)',
                         '[6.0, 7.5)',
                         '[6.0, 7.5)',
                         '[7.5, 9]',
                         '[7.5, 9]']
        
        self.output4 = ['[0, 1.8)',
                         '[0, 1.8)',
                         '[1.8, 3.6)',
                         '[1.8, 3.6)',
                         '[3.6, 5.4)',
                         '[3.6, 5.4)',
                         '[5.4, 7.2)',
                         '[5.4, 7.2)',
                         '[7.2, 9]',
                         '[7.2, 9]']
        
        self.output5 = ['[0, 3.8)',
                         '[0, 3.8)',
                         '[0, 3.8)',
                         '[0, 3.8)',
                         '[3.8, 7.6)',
                         '[3.8, 7.6)',
                         '[3.8, 7.6)',
                         '[3.8, 7.6)',
                         '[7.6, 11.4)',
                         '[7.6, 11.4)',
                         '[7.6, 11.4)',
                         '[7.6, 11.4)',
                         '[11.4, 15.2)',
                         '[11.4, 15.2)',
                         '[11.4, 15.2)',
                         '[11.4, 15.2)',
                         '[15.2, 19]',
                         '[15.2, 19]',
                         '[15.2, 19]',
                         '[15.2, 19]']
        

    def test_create_buckets(self):
        
        self.assertEqual(buckets(list(range(30)), 6), self.output1)
        self.assertEqual(buckets(list(range(20)), 6), self.output2)
        self.assertEqual(buckets(list(range(10)), 6), self.output3)
        self.assertEqual(buckets(list(range(10)), 5), self.output4)
        self.assertEqual(buckets(list(range(20)), 5), self.output5)

        
    def tearDown(self):
        print("Finished testing the test case.")

        
    @classmethod
    def tearDownClass(cls):
        print("Destroying TestCreateBuckets object")
        