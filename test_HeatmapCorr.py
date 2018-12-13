import unittest 
import pandas as pd 
import numpy as np
import os 
import sys

parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
import jootang.visual.heatmapCorr as hm

class TestHeatmapCorr(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initiate Test Heatmap for correlation")
        
    def setUp(self):
        self.testdf=pd.read_csv("data/beer.csv")  

        
                   
    def test_HeatmapCorr(self):  
        #test if heatmapCorr generates plots with different data sets

        self.assertIsNone(np.all(hm.heatmapCorr(self.testdf, 'price', 'mmmm')))
        
        self.assertTrue(np.all(hm.heatmapCorr(self.testdf, 'price', 'bitter') == np.array([1,0.8,0.8,1]).reshape((2,2))))
       
        self.assertTrue(np.all(hm.heatmapCorr(self.testdf, 'price', 'malty') == np.array([1,0.71,0.71,1]).reshape((2,2))))
        
        self.assertTrue(np.all(hm.heatmapCorr(self.testdf, 'price', 'cal') == np.array([1,0.42,0.42,1]).reshape((2,2))))
        
        self.assertTrue(np.all(hm.heatmapCorr(self.testdf, 'price', 'alc') == np.array([1,0.3,0.3,1]).reshape((2,2))))

        
    def tearDown(self):
        print("Finish testing")
    @classmethod
    def tearDownClass(cls):
        print("Done")
