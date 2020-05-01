class Matrix:

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        string = ''
        for i in self.lst:
                for j in i:
                    string = string + f'%s\t' % (j)
                string = string + '\n'
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.lst)):
            for j in range(len(self.lst[0])):
                summa = other.lst[i][j] + self.lst[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.lst[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

a = [[31, 22], [37, 43], [51, 86]]
b = [[11, 12], [7, 8], [2, 3]]

m1 = Matrix(a)
m2 = Matrix(b)

print(m1.__str__())
print(m2.__str__())

print(m1 + m2)


# задание 2 - пошив одежды

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def consumption(self):
        return self.size / 6.5 + 0.5

class Suit(Clothes):

    def __init__(self, length):
        self.__length = length

    @property
    def length(self):
        return self.__length

    def consumption(self):
        return 2 * self.length + 0.3

# coat = Coat(200)
# print(f'на пальто израсходновано: {coat.consumption()} метров')

# suit = Suit(150)
# print(f'на костюм израсходовано: {suit.consumption()} метров')


# задание третье - Клетка

class Cell:

    def __init__(self, q_cell):
        self.q_cell = int(q_cell)

    def __add__(self, other):
        return f'Сумма ячеек двух клеток: {self.q_cell + other.q_cell}'

    def __sub__(self, other):
        sub = self.q_cell - other.q_cell
        return f'Разность ячеек двух клеток: {sub if sub > 0 else "Не получается"}'

    def __mul__(self, other):
        mul = self.q_cell * other.q_cell
        return f'Произведение ячеек двух клеток: {mul}'

    def __truediv__(self, other):
        truediv = round(self.q_cell / other.q_cell)
        return f'Деление ячеек двух клеток: {truediv}'

    def make_order(self, cell_in_row):  # количество клеток в ряду
        self.string = ""
        while self.q_cell > 0:
            self.q_cell -= cell_in_row
            if self.q_cell < 0:
                self.string += ("*" * (cell_in_row + self.q_cell) + "\n")
            else:
                self.string += ("*" * cell_in_row + "\n")
        return self.string

""" супер упрощенная форма записи(как 2 вариант)
def make_order_2(self, cell_in_row):
self.str_1 = ""
i = 0
for elem in range(self.q_cell):
self.str_1 += "*"
i += 1
if i % cell_in_row == 0:
self.str_1 += "\n"
return self.str_1
"""

# c_1 = Cell(56)
# c_2 = Cell(10)
# print(c_1 + c_2)
# print(c_1 - c_2)
# print(c_1 / c_2)
# print(c_1 * c_2)
##print(c_1.make_order_2(9))
# print(c_1.make_order(10))
