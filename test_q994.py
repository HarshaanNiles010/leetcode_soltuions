import unittest
from q994 import calc_time

class TestRottingOranges(unittest.TestCase):
    def test_example1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        self.assertEqual(calc_time([row[:] for row in grid]), 4)

    def test_example2(self):
        grid = [[0,2]]
        self.assertEqual(calc_time([row[:] for row in grid]), 0)

    def test_impossible(self):
        grid = [[1,0,2]]
        self.assertEqual(calc_time([row[:] for row in grid]), -1)

if __name__ == '__main__':
    unittest.main()
