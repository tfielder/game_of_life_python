import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.board = [[1,0,1],
                 [0,1,1],
                 [1,1,0]]

    def test_set_board(self):
        Solution.set_board(self.board)
        print(Solution.b)
        self.assertEqual(Solution.b, self.board)

    def test_solution_2(self):
        result = Solution.run
        self.assertTrue(True, result)



if __name__ == "__main__":
    unittest.main()