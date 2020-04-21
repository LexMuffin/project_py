# ЗАДАНИЕ ПЕРВОЕ - расчет заработной платы

def income_salary(wk_hours, sal_per_hour, bonus):
    income = wk_hours * sal_per_hour
    if wk_hours > 120:
        income = income + bonus
    else:
        print("В этот раз без премии)")
    total_income = income * 0.87
    return total_income

print(income_salary(130, 200, 5000))


# ЗАДАНИЕ ВТОРОЕ - список чисел, которые меньше последующего

from random import shuffle

def num_list_1(a, b, c = 1):
    list_1 = [el for el in range(a, b, c)]
    shuffle(list_1)
    new_list_3 = []
    for i in range(len(list_1) - 1):
        x = int(list_1[i])
        i += 1
        y = int(list_1[i])
        if y > x:
            x = y
            new_list_3.append(y)
    return new_list_3

print(num_list_1(0, 20))


# ЗАДАНИЕ ТРЕТЬЕ - кратность на 20 и 21

new_list_1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(new_list_1)


# ЗАДАНИЕ ЧЕТВЕРТОЕ - вывести числа не имеющие повторения

# решение с помозью генератора
list_1 = [1, 2, 3, 4, 2, 6, 7, 3, 1]
used = set()
unique_list_1 = [x for x in list_1 if x not in used and (used.add(x) or True)]
print(unique_list_1)

# решение с помощью модуля Counter
from collections import Counter

list_2 = [1, 2, 4, 5, 6, 2, 5, 2]
counter = Counter(list_2)
unique = list(counter)
print(unique)

# ЗАДАНИЕ ПЯТОЕ - вывод четных чисел от 100 до 1000 и подсчет их произведения

# отдельно задать список и посчитать произведение
from functools import reduce

list_3 = [itm for itm in range(100, 1001) if not itm & 1]
print(list_3)
pow_list_3 = reduce(lambda x, y: x * y , list_3)
print(f'Произведение: {pow_list_3}')

# в одну строчку
pow_list_4 = reduce((lambda x, y: x * y), (itm for itm in range(100, 1001) if not itm & 1))
print(f'Произведение: {pow_list_4}')

# или же
pow_list_4 = reduce(lambda x, y: x * y, range(100, 1001, 2))
print(pow_list_4)

# ЗАДАНИЕ ШЕСТОЕ - итератор чисел

# a) бесконечный итератор, генерирующий целые числа, начиная с указанного(можно указать задержку счета)

from itertools import count
from time import sleep

def iter_count(start_num, num_step, delay=1):
    for i in count(start_num, num_step):
        print(i)
        sleep(delay)

iter_count(1, 2)

# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного ранее

from itertools import cycle
from time import sleep

def iter_cycle(list_4, delay=1):
    count_cycle = 0
    for i in cycle(list_4):
        print(i)
        sleep(delay)
        if  i == list_4[-1]:
            count_cycle += 1
            print(f'Список выведен {count_cycle} раз(а)')
            sleep(delay)

iter_cycle(["Привет", "Как дела?", "Нормально!"])

# ЗАДАНИЕ ШЕСТОЕ - генератор факториала

def fibo_gen(n):
    for i in range(1, n):
        yield i

factorial = 1
for el in fibo_gen(16):
    factorial *= el
    print(factorial)
