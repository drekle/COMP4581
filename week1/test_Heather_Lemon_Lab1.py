
from unittest import TestCase
import numpy as np

class TestLab1(unittest.TestCase):

    def test_print_matrix(self):
        self.fail()

    def test_matrix_multiply(self):
        # Test1
        A = [[2, -3, 3],
             [-2, 6, 5],
             [4, 7, 8]]
        B = [[-1, 9, 1],
             [0, 6, 5],
             [3, 4, 7]]
        C = matrixMult(A, B)
        if not C == None:
            printMatrix(C)
    # def test_uneven_innerRow(self):
    #     # Test2
    #     A = [[2, -3, 3, 0],
    #          [-2, 6, 5, 1],
    #          [4, 7, 8, 2]]
    #     B = [[-1, 9, 1],
    #          [0, 6, 5],
    #          [3, 4, 7]]
    #     C = matrixMult(A, B)
    #     if not C == None:
    #         printMatrix(C)
    # def test_larger_matrix(self):
    #     # Test3
    #     A = [[2, -3, 3, 5],
    #          [-2, 6, 5, -2]]
    #     B = [[-1, 9, 1],
    #          [0, 6, 5],
    #          [3, 4, 7],
    #          [1, 2, 3]]
    #     C = matrixMult(A, B)
    #     if not C == None:
    #         printMatrix(C)
    def check_math(self):
        result = np.dot(A,B)
        print(result)

if __name__ == '__main__':
    unittest.TestCase()