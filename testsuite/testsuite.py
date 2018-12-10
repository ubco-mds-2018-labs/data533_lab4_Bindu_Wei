import unittest 
from .unittests.test_HeatmapCorr import TestHeatmapCorr
from .unittests.test_HeatmapCorr3 import TestHeatmapCorr3
from .unittests.test_create_buckets import TestCreateBuckets
from .unittests.test_addone import TestAddone

def testsuite(): 
    suite = unittest.TestSuite() 
    result = unittest.TestResult() 
    suite.addTest(unittest.makeSuite(TestHeatmapCorr)) 
    suite.addTest(unittest.makeSuite(TestHeatmapCorr3))
    suite.addTest(unittest.makeSuite(TestCreateBuckets))
    suite.addTest(unittest.makeSuite(TestAddone))
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
