import os.path
import unittest
from hw_6 import sqrff

"""Consider that we have some float numbers as desired values: 0.81 (as 9/13), 0.85 and 1.46 (as 19/13) """
testable_vars = [0.81, 0.85, 1.46]
fpath = "C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/reality.txt"

os.path.isfile(fpath)


class TestTryTree(unittest.TestCase):
    def test_sqr_function(self):
        sqrff(fpath)
        result = open(fpath, 'r')
        res = result.read().split()
        msg = "not equal"
        for i in range(len(res)):
            self.assertAlmostEqual(float(res[i]), testable_vars[i], None, msg, 0.01)
