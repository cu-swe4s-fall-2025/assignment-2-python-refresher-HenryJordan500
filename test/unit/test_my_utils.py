import src.my_utils as my_utils
import unittest
import numpy as np

class MeanTest(unittest.TestCase):

    def test_mean_value(self):

        test_arr = np.random.randint(100,size=10)

        self.assertAlmostEqual(np.mean(test_arr), my_utils.mean(test_arr))
    
    def test_valid_length(self):

        arr = []

        self.assertRaises(ValueError, my_utils.mean, arr)


class MedianTest(unittest.TestCase):

    def test_median_value(self):

        odd_len_arr = np.random.randint(100,size=11)
        even_len_arr = np.random.randint(100,size=10)

        self.assertAlmostEqual(np.median(odd_len_arr), my_utils.median(odd_len_arr))
        self.assertAlmostEqual(np.median(even_len_arr), my_utils.median(even_len_arr))
    
    def test_valid_length(self):
        
        arr = []

        self.assertRaises(ValueError, my_utils.median, arr)
    

class StdTest(unittest.TestCase):

    def test_std_value(self):

        test_arr = np.random.randint(100, size=1000)

        self.assertAlmostEqual(np.std(test_arr), my_utils.std(test_arr))
    
    def test_valid_length(self):

        arr = []

        self.assertRaises(ValueError, my_utils.std, arr)

if __name__ =='__main__':
    unittest.main()