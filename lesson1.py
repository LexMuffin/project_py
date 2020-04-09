# задание первое - работа с переменными

# работа с числами
"""
first_variable = int(input("Введите первую переменную\n"))
second_variable = int(input("Введите вторую переменную\n"))
sum_vars = first_variable + second_variable
print("Сумма = {}" .format(sum_vars))
"""

# работа со строками
"""
first_str = 'Прощай'
second_str = 'жестокий мир'
new_str = print(first_str + " " + second_str)
print(f'{first_str} этот {second_str}')
"""

# задание второе - перевод секунд в формат чч:мм:сс

"""
seconds = int(input("Введите время в секундах\n"))
hours = seconds // (60*60)
seconds %= (60*60)
minutes = seconds // 60
seconds %= 60
print(f'{hours}:{minutes}:{seconds}')
"""

# задание третье - найти сумму в формате n + nn + nnn

"""
n = int(input("Введите число n\n"))
n_n = n * 10 + n
n_n_n = n * 100 + n * 10 + n
sum_of_n = n + n_n + n_n_n
print(f'{n} + {n_n} + {n_n_n} = {sum_of_n}')
"""

# задание четвертое - найти самую большую цифру в числе

# немного емкий получился(рациональней было бы ввести функцию)
"""
num_1 = int(input("Введите число\n"))
if num_1 < 0 :
    num_1 = int(input("Введите положительное число\n"))
    a = 0
    while num_1 > 0:
        c = num_1 % 10
        if c >= a:
            a = c
        num_1 = num_1 // 10
    print(a)
else:
    a = 0
    while num_1 > 0:
        c = num_1 % 10
        if c >= a:
            a = c
        num_1 = num_1 // 10
    print(a)
"""


# задание пятое - выручка и прибыль

# ввел round, потому что много знаков после запятой было
"""
profit = int(input("Введите прибыль компании\n"))
costs = int(input("Введите издержки компании\n"))
revenue = profit - costs
if revenue > 0:
    print("У вас прибыльное дело")
    profitability = round(revenue / profit, 5)
    num_workers = int(input("Введите количество сотрудников\n"))
    prof_worker = round(profitability / num_workers, 5)
    print(f'рентабельность = {profitability}, прибыль на сотрудника = {prof_worker}')
elif revenue < 0:
    print("Вы терпите крах")
"""

# задание шестое - спортсмен и пробежки

# 1 вариант
"""
cur_day = int(input("Введите результат в первый день\n"))
purpose = int(input("Введите ожидаемый общий результат\n"))
days = 1
while purpose > cur_day:
    cur_day += cur_day * 0.1
    days += 1
    if cur_day >= b:
        print(days)
    else:
        continue
"""

# 2 вариант
"""
cur_day = int(input("Введите результат в первый день\n"))
purpose = int(input("Введите ожидаемый общий результат\n"))
days = 1
while purpose - cur_day >= 0:
    cur_day += cur_day * 0.1
    days += 1
print(days)
"""

