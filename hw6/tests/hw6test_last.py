import unittest
from hw_6 import replace_content
import pickle

filepath1 = "C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/bin1.bin"
filepath2 = "C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/bin2.bin"
'''A contain of dump Variables bin1 = ["moisture", 96, "pickle"] and
bin2 = ("w", "ist", "S") should be replaced after function implementing'''


class TestTryTree(unittest.TestCase):
    def test_cross_rplacement(self):
        actual1 = ["moisture", 96, "pickle"]
        actual2 = ["w", "ist", "S"]
        file1 = open(filepath1, 'rb')
        file2 = open(filepath2, 'rb')
        replace_content(actual1, actual2)
        result1 = pickle.load(file1)
        result2 = pickle.load(file2)
        assert all([a == b for a, b in zip(actual1, result2)])
        assert all([a == b for a, b in zip(actual2, result1)])
