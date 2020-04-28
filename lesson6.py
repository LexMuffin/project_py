# задание первое - светофор

# один из вариантов
"""
from time import sleep

class TrafficLight:
    __color = "Светофор"

    def running(self):
        while True:
            self.__color = "красный"
            print(self.__color)
            sleep(7)
            self.__color = "желтый"
            print(self.__color)
            sleep(2)
            self.__color = "зеленый"
            print(self.__color)
            sleep(5)

#traffic = TrafficLight()
#traffic.running()
"""
# второй вариант

from time import sleep

class TrafficLight:
    __color = "Светофор"

    def running(self):
        while True:
            print("красный")
            sleep(7)
            print("желтый")
            sleep(2)
            print("зеленый")
            sleep(5)

traffic = TrafficLight()
traffic.running()

# задание второе - рассчет асфальта

class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, mass, thickness):
        self._length = _length
        self._width = _width
        self.mass = mass
        self.thickness = thickness

    def mass_assert(self):
        leng = self._length
        wid = self._width
        m = self.mass
        thick = self.thickness
        result = int((leng * wid * m * thick) / 1000)
        return print("Масса: {}м * {}м * {}кг * {}см = {}т ".format(leng, wid, m, thick, result))

r = Road(20, 5000, 25, 5)
r.mass_assert()

# задание третье - работник и зарплата

class Worker:
    name = "Михаил"
    surname = "Зубенко"
    position = "Вор в законе"
    salary = 50000
    bonus = 10000
    _income = {"Оклад": salary,
               "Премия": bonus,
    }
    res_profit = 0

class Position(Worker):

    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Должность: {self.position}'

    def get_total_income(self):
        res_profit = self._income["Оклад"] + self._income["Премия"]
        return "Зарплата с учетом премии: {} руб.".format(res_profit)

w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.salary)

p = Position()
print(p.get_full_name())
print(p.get_total_income())

# задание четвертое -  про машины

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def info_car(self):
        return f'Машина {self.name}, {self.color} оттенка, едет со скоростью {self.speed} км/ч'

    def police(self):
        if self.is_police:
            return "Полицеская машина"
        else:
            return "Гражданская машина"

    def go(self):
        if self.speed != 0:
            return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, side):
        if side == 1:
            return "Машина повернула налево"
        elif side == 2:
            return "Машина повернула направо"

    def show_speed(self):
        return f'{self.speed} км/ч - текущая скорость авто'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость - {self.speed}, превышающая правила ПДД'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение допустимой скорости'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_c = TownCar(70, "синяя", "Kia", False)
print(t_c.police() + "\n" + t_c.info_car() + "\n" + t_c.go() + "\n" + t_c.turn(1))
print(t_c.show_speed())
print(t_c.stop())
print("-------------------------------------------------------------------------")

s_c = SportCar(100, "черная", "Nissan", False)
print(s_c.police() + "\n" + s_c.info_car() + "\n" + s_c.go() + "\n" + s_c.turn(2) + "\n" + s_c.show_speed())
print("-------------------------------------------------------------------------")

w_c = WorkCar(50, "красная", "Renault", False)
print(w_c.police() + "\n" + w_c.info_car() + "\n" + w_c.go() + "\n" + w_c.turn(1))
print(w_c.turn(2))
print(w_c.stop())
print("-------------------------------------------------------------------------")

p_c = PoliceCar(50, "бело-синяя", "Ford", True)
print(p_c.police() + "\n" + p_c.info_car() + "\n" + p_c.go() + "\n" + p_c.turn(2))
print(p_c.stop())
print("-------------------------------------------------------------------------")


#задание пятое - метод Stationery

class Stationery:
    title = "Канцелярский атрибут"

    def draw(self):
        print("метод Stationery от которого наследуется")
        print('Запуск отрисовки\n')

class Pen(Stationery):

    def draw(self):
        print("метод Pen")
        print("Запуск отрисовки ручкой\n")

class Pencil(Stationery):

    def draw(self):
        print("метод Pencil")
        print("Запуск отрисовки карандашом\n")

class Handle(Stationery):

    def draw(self):
        print("метод Handle")
        print("Запуск отрисовки маркером")

s = Stationery()
print(s.title)
s.draw()

p = Pen()
p.draw()

pencil = Pencil()
pencil.draw()

h = Handle()
h.draw()
