from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    @staticmethod
    def transposed(matrix):
        rows, columns = matrix.size()
        newMatrixValues = [[0] * rows for _ in range(columns)]
        for row in range(rows):
            for column in range(columns):
                newMatrixValues[column][row] = matrix.matrixValues[row][column]
        return Matrix(newMatrixValues)

    def __init__(self, listOfLists):
        self.rows = len(listOfLists)
        self.columns = len(listOfLists[0])
        self.matrixValues = [row.copy() for row in listOfLists]

    def __str__(self):
        result = ''
        for row in self.matrixValues:
            result += '\t'.join(map(str, row)) + '\n'
        return result[:-1]

    def size(self):
        return (self.rows, self.columns)

    def __add__(self, leftMatrix):
        if self.size() != leftMatrix.size():
            raise MatrixError(self, leftMatrix)
        newMatrixValues = [[0] * self.columns for _ in range(self.rows)]
        for row in range(self.rows):
            for column in range(self.columns):
                elementSum = (leftMatrix.matrixValues[row][column] +
                              self.matrixValues[row][column])
                newMatrixValues[row][column] = elementSum
        return Matrix(newMatrixValues)

    def __mul__(self, other):
        rows1, columns1 = self.size()

        if isinstance(other, Matrix):
            rows2, columns2 = other.size()
            if columns1 != rows2:
                raise MatrixError(self, other)

            newMatrixValues = [[0] * columns2 for _ in range(rows1)]
            for i in range(rows1):
                for j in range(columns2):
                    for k in range(columns1):
                        newMatrixValues[i][j] += (self.matrixValues[i][k] *
                                                  other.matrixValues[k][j])
            return Matrix(newMatrixValues)
        else:
            newMatrix = Matrix(self.matrixValues)
            for row in range(self.rows):
                for column in range(self.columns):
                    newMatrix.matrixValues[row][column] *= other
            return newMatrix

    def __rmul__(self, other):
        return self.__mul__(other)

    def transpose(self):
        transposedMatrix = Matrix.transposed(self)
        self.__init__(transposedMatrix.matrixValues)
        return transposedMatrix


exec(stdin.read())
