"""
Heather Lemon
COMP 4581
6/6/2022
Lab 1 - Matrix Multiply
"""

import math
import statistics

import numpy as np

"""
matrix multiply with NxN
"""
class Lab1:

    def __init__(self, A, B):
        """
        Init empty matrix
        """
        self.matrixA = A
        self.matrixB = B
        self.matrixC = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    def checkDimension(self, A, B):
        """
        check that the inner dimesions are the same
        :param A: matrix A
        :param B: matrix B
        :return: True if same, False otherwise
        """
        rowsA = len(self.matrixA)
        columnsA = len(self.matrixA[0])
        rowsB = len(self.matrixB)
        columnsB = len(self.matrixB[0])
        if columnsA == rowsB:
            return True
        else:
            return False

    def printMatrixA(self):
        """
        pretty print matrix A
        :return: None
        """
        for row in self.matrixA:
            print(row)

    def printMatrixB(self):
        """
        pretty print matrix B
        :return: None
        """
        for row in self.matrixB:
            print(row)

    def printMatrixC(self):
        """
        pretty print matrix C
        :return: None
        """
        for row in self.matrixC:
            print(row)

    def matrixMult(self, A, B):
        print("start matrix multiply")
        C = np.dot(A,B)
        # print(C)
        # self.printMatrixA()
        # self.printMatrixB()
        # rows of A
        for A_index in A:
            # cols of B
            for B_index in B:
                matrix_sum = 0
                c = matrix_sum + A[0:] * B[:, 0]
            C_index[A_index, B_index] = c
        return self.matrixC

if __name__ == '__main__':
    A = [[2, -3, 3],
         [-2, 6, 5],
         [4, 7, 8]]
    B = [[-1, 9, 1],
         [0, 6, 5],
         [3, 4, 7]]
    lab1 = Lab1(A, B)
    isTrue = lab1.checkDimension(A, B)
    if isTrue:
        lab1.matrixMult(A, B)
    else:
        print("Cannot multiply matrix A x B as the inner dimensions "
              "are not the same size.")
