# Created by Anita Kuzmina
# class_Matrix
# 02.12.2018

from sys import stdin


class Matrix:
    matrixVal = []
    matrixRows = 0
    matrixColumns = 0

    def __init__(self, listOfLists):
        self.matrixVal = listOfLists
        self.matrixRows = len(self.matrixVal)
        self.matrixColumns = len(self.matrixVal[0])

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrixVal)

    def size(self):
        return self.matrixRows, self.matrixColumns

    def __getitem__(self, elem):
        return self.matrixVal[elem]

    def add(self, matrixToAdd):
        matrixToAdd = Matrix(matrixToAdd)
        result = []
        numbers = []
        for i in range(len(self.matrixVal)):
            for j in range(len(self.matrixVal[0])):
                matrixSum = matrixToAdd[i][j] + self.matrixVal[i][j]
                numbers.append(matrixSum)
                if len(numbers) == len(self.matrixVal):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def mul(self, scalar):
        if isinstance(scalar, (int, float)):
            result = [[scalar * x for x in y] for y in self.matrixVal]
            return Matrix(result)
        elif self.matrixColumns != scalar.matrixRows:
            print('Error! Matrix dimensions do not match')
        else:
            firstMatrixCols = range(self.matrixColumns)
            firstMatrixRows = range(self.matrixRows)
            scalarCols = range(scalar.matrixColumns)
            result = []
            for i in firstMatrixRows:
                res = []
                for j in scalarCols:
                    elem = 0
                    for k in firstMatrixCols:
                        elem += self.matrixVal[i][k] * scalar.matrixVal[k][j]
                    res.append(elem)
                result.append(res)
            return Matrix(result)

    def rmul(self, scalar):
        return self.mul(scalar)


exec(stdin.read())
