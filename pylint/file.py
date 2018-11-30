from sys import stdin
from copy import copy, deepcopy


class MatrixError(Exception):
    matrix1 = None
    matrix2 = None

    def __init__(self, message, mt1=None, mt2=None):
        super().__init__(message)
        self.matrix1 = mt1
        self.matrix2 = mt2


class Matrix:
    mt = [[]]
    shape = ()

    def __init__(self, mt=[], shape=(-1, -1)):
        if len(mt) != 0:
            self.mt = deepcopy(mt)
            self.shape = (len(self.mt), len(self.mt[0]))
        else:
            self.shape = copy(shape)
            self.mt = [[0 for row in range(self.shape[1])]
                       for col in range(self.shape[0])]

    def printMe(self, tabs=6):
        for row in self.mt:
            print(*(str(el).ljust(tabs) for el in row))

    def __add__(self, other):
        if other.shape != self.shape:
            raise MatrixError("You can't sum up not equal size matrixes",
                              self, other)
        new_matrix = Matrix(shape=self.shape)
        rows, columns = self.shape
        for row in range(0, rows):
            for column in range(0, columns):
                new_matrix.mt[row][column] = self.mt[row][column] \
                                             + other.mt[row][column]
        return new_matrix

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if other.shape != self.shape:
            raise MatrixError("You can't substract not equal size matrixes",
                              self, other)
        new_matrix = Matrix(shape=self.shape)
        rows, columns = self.shape
        for row in range(0, rows):
            for column in range(0, columns):
                new_matrix.mt[row][column] = self.mt[row][column] \
                                             - other.mt[row][column]
        return new_matrix

    def __rsub__(self, other):
        return -1 * self.__sub__(other)

    def __mul__(self, other):
        if type(other) == Matrix:
            if self.shape[1] != other.shape[0]:
                raise MatrixError("You can't multiply matrixes with sizes \
                        ({}) and ({})".format(self.shape, other.shape),
                                  self, other)
            new_matrix = Matrix(shape=(self.shape[0], other.shape[1]))
            for i in range(self.shape[0]):
                for j in range(other.shape[1]):
                    for k in range(self.shape[1]):
                        new_matrix.mt[i][j] += self.mt[i][k] * other.mt[k][j]
            return new_matrix
        else:
            new_matrix = Matrix(shape=(self.shape[0], self.shape[1]))
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix.mt[i][j] += self.mt[i][j] * other
            return new_matrix

    def __rmul__(self, other):
        if type(other) == Matrix:
            if other.shape[1] != self.shape[0]:
                raise MatrixError("You can't multiply matrixes with sizes \
                        ({}) and ({})".format(self.shape, other.shape),
                                  self, other)
            new_matrix = Matrix(shape=(other.shape[0], self.shape[1]))
            for i in range(other.shape[0]):
                for j in range(self.shape[1]):
                    for k in range(other.shape[1]):
                        new_matrix.mt[i][j] += other.mt[i][k] * self.mt[k][j]
            return new_matrix
        else:
            new_matrix = Matrix(shape=(self.shape[0], self.shape[1]))
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix.mt[i][j] += self.mt[i][j] * other
            return new_matrix

    def toRowEchelonForm(self):
        # ???????, ??????? ????? ????????
        j = 0
        # ????????? ?? ???????? ?? ???-?? ????? ? ???-?? ????????
        for repeat in range(0, min(self.shape[0], self.shape[1])):
            # ????? ?????? ? ??????? j-?? ??????? ?? ???????
            i = -1
            # ?????????? ??????, ???? ? ????????? j-?? ?????????
            for row in range(j, self.shape[0]):
                if self.mt[row][j] != 0:
                    i = row
                    break
            # ???? ????? ?????? ? ??????? j-?? ??????? ?? ????
            if i != -1:
                # ?????????? ? j-?? ???????
                self.mt[i], self.mt[j] = self.mt[j], self.mt[i]
                # ???? ?? ???? ??????? ??????? ??????? ? j + 1
                for row in range(j + 1, self.shape[0]):
                    alpha = self.mt[row][j] / self.mt[j][j]
                    for col in range(j, self.shape[1]):
                        self.mt[row][col] -= self.mt[j][col] * alpha
            j += 1

    def solve(self, b):
        if self.shape[1] != self.shape[0]:
            raise MatrixError('Infinity or zero solutions')
        sm = Matrix(self.mt)
        for i in range(0, sm.shape[0]):
            sm.mt[i].append(b[i])
        sm.shape = (sm.shape[0], sm.shape[1] + 1)
        sm.toRowEchelonForm()
        solution = [None] * len(self.mt)
        for i in range(sm.shape[0] - 1, -1, -1):
            for j in range(i + 1, sm.shape[1] - 1):
                if solution[j] is None:
                    raise MatrixError('Infinity or zero solutions')
                else:
                    sm.mt[i][sm.shape[1] - 1] -= solution[j] * sm.mt[i][j]
            if sm.mt[i][sm.shape[1] - 1] != 0:
                solution[i] = sm.mt[i][sm.shape[1] - 1] / sm.mt[i][i]
        return solution

    def transpose(self):
        new_matrix = Matrix.transposed(self)
        self.mt = new_matrix.mt
        self.shape = new_matrix.shape
        return self

    @staticmethod
    def transposed(x):
        new_matrix = Matrix(shape=(x.shape[1], x.shape[0]))
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                new_matrix.mt[j][i] = x.mt[i][j]
        return new_matrix

    @staticmethod
    def E(shape=(1, 1)):
        toReturn = Matrix(shape=shape)
        for i in range(0, min(shape[0], shape[1])):
            toReturn.mt[i][i] = 1
        return toReturn

    def size(self):
        return self.shape

    def __str__(self):
        toReturn = ''
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                toReturn += str(self.mt[i][j])
                if j != self.shape[1] - 1:
                    toReturn += '\t'
            if i != self.shape[0] - 1:
                toReturn += '\n'
        return toReturn

    def tr(self):
        trail = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if i == j:
                    trail += self.mt[i][j]
        return trail


class SquareMatrix(Matrix):

    def __init__(self, mt=[], shape=(-1, -1)):
        if len(mt) != len(mt[0]) or shape[0] != shape[1]:
            raise MatrixError("That's not a square matrix")
        super().__init__(mt, shape)

    def __pow__(self, toPow):
        n = toPow
        res = Matrix.E(self.shape)
        A = Matrix(self.mt)
        while n > 0:
            if n % 2:
                res = res * A
            A = A * A
            n //= 2
        return res


exec(stdin.read())
