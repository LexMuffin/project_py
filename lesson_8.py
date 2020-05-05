# задание первое - дата
class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def transform(cls, date: str):
        day, month, year = map(int, date.split("-"))
        print(cls, day, month, year)

    @staticmethod
    def validation(date: str):
        day, month, year = map(int, date.split("-"))
        if 0 <= day <= 31 and 0 <= month <= 12 and year <= 2020:
            print(date)
            return day, month, year
        else:
            return "Введена некорректная дата"

d_1 = '21-11-1900'
date_1 = Date.transform(d_1)
print(Date.validation(d_1))

d_2 = '33-12-2000'
date_2 = Date.transform(d_2)
print(Date.validation(d_2))

# задание второе - создание класса исключения

class OwnError(Exception):

    def div_num(self, a, b):
        try:
            div = a / b
        except TypeError:
            print(f"{a} / {b} - Нельзя выполнять деление не с числами")
        except ZeroDivisionError:
            print(f"{a} / {b} - Делить на ноль нельзя")
        else:
            print(f'{a} / {b} = {div}')

exc = OwnError()
exc.div_num(10, 0)
exc.div_num(15, "пять")
exc.div_num(100, 5)

# задание третье - метод ошибки-исключения

class MyError(Exception):

    def err_check(self):
        lst = []
        start = 0
        finish = 100
        while True:
            try:
                for i in range(start, finish):
                    elem = input("элемент спика: ")
                    if elem.isdigit():
                        print(f'добавляем {elem} в список')
                        lst.append(int(elem))
                    elif elem == "stop":
                        return lst
                    else:
                        raise MyError(f'{elem} - не число. В список добавлено не будет')
            except MyError as err:
                print(err)
                start = i

err = MyError()
print(err.err_check())

# задания четвертое:шестое - орг техника
class OfficeTechniques:
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color

class Printer(OfficeTechniques):
    amount_pr = 0
    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "Printer"

    def pr_type(self):
        return self.pr_type

    def __str__(self):
        return f'Производитель: {self.producer}, цвет: {self.color}, тип: {self.pr_type}'

class Scanner(OfficeTechniques):
    def __init__(self, producer, color, sensor):
        super().__init__(producer, color)
        self.sensor = sensor

    @staticmethod
    def name():
        return 'Scanner'

    def sensor(self):
        return self.sensor

    def __str__(self):
        return f'Производитель: {self.producer}, цвет: {self.color}, сенсор: {self.sensor}'

class Xerox(OfficeTechniques):
    def __init__(self, producer, color, max_connect):
        super().__init__(producer, color)
        self.max_connect = max_connect

    @staticmethod
    def name():
        return 'Xerox'

    def max_connect(self):
        return self.max_connect

    def __str__(self):
        return f'Производитель: {self.producer}, цвет: {self.color}, макс. подключений: {self.max_connect}'

p1 = Printer("HP", "black", "laser")
p2 = Printer("Canon", "silver", "inkjet")
print(p1.name(), p1.amount_pr, "шт.")
print(p1.__str__())
print(p2.__str__())

s1 = Scanner("HP", "black", "CIS")
s2 = Scanner("Canon", "silver", "CMOS")
print(s1.name())
print(s1.__str__())
print(s2.__str__())

x1 = Xerox("HP", "black", 10)
x2 = Xerox("Canon", "silver", 20)
print(x1.name())
print(x1.__str__())
print(x2.__str__())

# задание седьмое - комплексные числа
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        sum_a = self.a + other.a
        sum_b = self.b + other.b
        return Complex(sum_a, sum_b)

    def __mul__(self, other):
        mul_a = self.a * other.a - self.b * other.b
        mul_b = self.a * other.b + self.b * other.a
        return Complex(mul_a, mul_b)

    def __truediv__(self, other):
        denominator = other.a ** 2 + other.b ** 2
        truediv_a = (self.a * other.a + self.b * other.b) / (denominator)
        truediv_b = (self.b * other.a - self.a * other.b) / (denominator)
        return Complex(truediv_a, truediv_b)

z1 = Complex(1, 4)
z2 = Complex(-3, 5)
print(f'{z1}, {z2} - комплексные числа')
print(f'{z1} + {z2} = {z1 + z2} (сложение)')
print(f'{z1} * {z2} = {z1 * z2} (умножение)')
print(f'{z1} / {z2} = {z1 / z2} (деление)')

print(f'{complex(1, 4) + complex(-3, 5)} - проверка сложения')
print(f'{complex(1, 4) * complex(-3, 5)} - проверка умножения')
print(f'{complex(1, 4) / complex(-3, 5)} - проверка деления')