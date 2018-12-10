import unittest 
import pandas as pd 
import numpy as np
import os 
import sys

parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
import jootang.visual.heatmapCorr3 as hm3

class TestHeatmapCorr3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initiate Test Heatmap for correlation")
        
    def setUp(self):
        self.testdf=pd.read_csv("data/beer.csv")  
                   
    def test_HeatmapCorr3(self):  
        #test if heatmapCorr generates plots with different data sets
        self.assertIsNone(np.all(hm3.heatmapCorr(self.testdf, 'price', 'mmmm', 'nnn')))
        
        self.assertTrue(np.all(hm3.heatmapCorr3(self.testdf, 'price', 'bitter', 'malty') == np.array([1,0.8,0.71,0.8,1,0.91,0.71,0.91,1]).reshape((3,3))))
        
        self.assertTrue(np.all(hm3.heatmapCorr3(self.testdf, 'price', 'malty', 'cal') == np.array([1,0.71,0.42,0.71,1,0.6,0.42,0.6,1]).reshape((3,3))))
        
        self.assertTrue(np.all(hm3.heatmapCorr3(self.testdf, 'price', 'cal', 'alc') == np.array([1,0.42,0.3,0.42,1,0.89,0.3,0.89,1]).reshape((3,3))))
        
        self.assertTrue(np.all(hm3.heatmapCorr3(self.testdf, 'price', 'alc', 'bitter') == np.array([1,0.3,0.8,0.3,1,0.48,0.8,0.48,1]).reshape((3,3))))
       
    def tearDown(self):
        print("Finish testing")
    @classmethod
    def tearDownClass(cls):
        print("Done")
