import unittest
import os
import random
import get_column_stats as g
import numpy as np


# function to make a file of random numbers, used for interation
# this function is only used for some of the tests
def filemaker(r1, r2, c):
    nums = 100*np.random.randint(low=0, high=100, size=(r2, r1))
    tmean = np.mean(nums[:, c])
    tstd = np.std(nums[:, c])
    test_file_name = 'test_file.txt'
    test_file = np.savetxt(test_file_name, nums)
    return test_file_name, round(tmean, 4), round(tstd, 4)


# unit tests for get_column_stats.py
class TestColStats(unittest.TestCase):

    # random file set up before all tests
    @classmethod
    def setUpClass(cls):
        cls.rand1 = random.randint(1, 10)
        rand2 = random.randint(1, 10)
        cls.colnum = random.randint(0, cls.rand1-1)

        nums = 100*np.random.randint(low=0, high=100, size=(rand2, cls.rand1))
        cls.tmean = sum(nums[:, cls.colnum])/len(nums[:, cls.colnum])
        print(cls.test_mean)

        cls.test_file_name = 'test_file.txt'
        cls.test_file = np.savetxt(cls.test_file_name, nums)

    # delete random file after tests
    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_name)

    # testing calculation of mean
    # iterates 100 times
    def test_mean(self):

        for i in range(100):
            rand1 = random.randint(1, 10)
            rand2 = random.randint(1, 10)
            colnum = random.randint(0, rand1-1)

            test_file_name, tmean, tstd = filemaker(rand1, rand2, colnum)
            mean, std = g.main(test_file_name, colnum)

            self.assertEqual(mean, tmean)

    # testing calculation of standard deviation
    # iterates 100 times
    def test_std(self):
        for i in range(100):
            rand1 = random.randint(1, 10)
            rand2 = random.randint(1, 10)
            colnum = random.randint(0, rand1-1)

            test_file_name, tmean, tstd = filemaker(rand1, rand2, colnum)
            mean, std = g.main(test_file_name, colnum)

            self.assertEqual(std, tstd)

    # testing exception for bad col num input
    def test_colnum_not_in_bounds(self):
        bad_col_num = self.rand1 + random.randint(1, 10)
        self.assertRaises(ValueError, g.main, self.test_file_name, bad_col_num)

    # testing exception for bad col num input
    def test_colnum_not_int(self):
        bad_col_num = self.colnum + 0.5
        self.assertRaises(ValueError, g.main, self.test_file_name, bad_col_num)


if __name__ == '__main__':
    unittest.main()
