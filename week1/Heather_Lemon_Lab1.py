
import os

class Matrix:

    '''
    '''
    def __init__(self, matrix : list[list[int]]):

        # separate our two dimensional array into rows and columns for helpers
        self.columns:list[list[int]] = []
        self.rows:list[list[int]] = []
        # each matrix row and column must be the same length
        # we don't care if they gave us column oriented or a row oriented array at this point
        xsize:int = 0
        for row in matrix:
            if xsize == 0:
                xsize = len(row)
                continue
            if xsize != len(row):
                raise ValueError("matrix constructor given rows of unequal length")

        # split the two dimensional into rows and columns as it will be easier to work with
        for row in matrix:
            self.rows.append(row)
            if len(self.columns) == 0:
                for i in range(0, len(row)):
                    col = [row[i] for row in matrix]
                    self.columns.append(col)

        self.matrix:list[list[int]] = matrix

    '''
    '''
    def getMatrix(self) -> list[list[int]]:
        return self.matrix
    
    '''
    '''
    def getRows(self) -> list[list[int]]:
        return self.rows

    '''
    '''
    def getColumns(self) -> list[list[int]]:
        return self.columns

    '''
    '''
    def checkConstraints(self, other : 'Matrix'):
        # this matrix column length must equal the row length of the second matrix
        cols = len(self.getColumns())
        rows = len(other.getRows())
        if cols != rows:
            print("constraints failed for self columns length " + str(cols) + " not equal to argument rows of length " + str(rows))
            os._exit(1)

    '''
    '''
    def multiply(self, other : 'Matrix') -> 'Matrix':
        self.checkConstraints(other)

        # helpers
        firstRows : list[int] = self.getRows()
        firstColumns : list[int] = self.getColumns()
        secondColumns : list[int] = other.getColumns()
        
        resArr : list[list[int]] = []
        for idx1 in range(0, len(firstRows)):
            rowContent : list[int] = []
            # idx corresponds to first column, or second row
            for idx2 in range(0, len(secondColumns)):
                value : int = 0
                for idx3 in range(0, len(firstColumns)):
                    aval = self.getMatrix()[idx1][idx3]
                    bval = other.getMatrix()[idx3][idx2]
                    value += aval * bval
                rowContent.append(value)
            resArr.append(rowContent)

        return Matrix(resArr)

        
    def __str__(self):
        s : str = ""
        # tabs look nicer
        for row in self.getRows():
            s += "[\t"
            for vIdx, v in enumerate(row):
                s += str(v)
                if vIdx == len(row) - 1:
                    s += "\t]" + os.linesep
                else:
                    # for commas
                    # s += ",\t"
                    s +="\t"
        return s

def test1():
    A = Matrix([
        [2,-3,3],
        [-2,6,5],
        [4,7,8]
        ])
    B = Matrix([
        [-1,9,1],
        [0,6,5],
        [3,4,7]
        ])
    return (A,B)

def test2():
    A = Matrix([
        [2,-3,3,0],
        [-2,6,5,1],
        [4,7,8,2]
        ])
    B = Matrix([
        [-1,9,1],
        [0,6,5],
        [3,4,7]
        ])
    return (A,B)

def test3():
    A = Matrix([
        [2,-3,3,5],
        [-2,6,5,-2]
        ])
    B = Matrix([
        [-1,9,1],
        [0,6,5],
        [3,4,7],
        [1,2,3]
        ])
    return (A,B)

def main():
    test = test3()
    result = test[0].multiply(test[1])
    print(test[0])
    print( "\t\t*")
    print(test[1])
    print( "\t\t=")
    print(result)

if __name__ == "__main__":
    main()