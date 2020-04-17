# задание первое - деление чисел

# первый вариант задания
def div_num():
    try:
        num_1 = int(input("Введите делимое\n"))
        num_2 = int(input("Введите делитель\n"))
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    except ValueError:
        print("Не введены данные")

print(div_num())

# второй вариант задания
def div_num_2(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    except ValueError:
        print("Не введены данные")

def div_num_input_2():
    print(div_num_2(int(input("Введите делимое: ")), int(input("Введите делитель: "))))

div_num_input_2()

# задание второе - вывод данных о пользователе

def person_data_1(**kwargs):
    return list(kwargs.values())

def person_data_input_1():
     print(person_data_1(name = input("Введите имя: "),
                         sur_name = input("Введите фамилию: "),
                         birth_date = input("Введите год рождения: "),
                         liv_town = input("Введите город проживания: "),
                         email = input("Введите почту: "),
                         tele = input("Введите телефонный номер: ")
                         ))

person_data_input_1()

# задание третье - найти максимум из двух чисел

def num_find(num_1, num_2, num_3):
    z = [num_1, num_2, num_3]
    z.remove(min(num_1, num_2, num_3))
    return sum(z)

res_sum = num_find(-50, 100, 70)
print(res_sum)

# задание четвертое - возведение числа в степень

# вариант 1 через **
def pow_num_1(x, y):
    return  x ** y

print(pow_num_1(2, -3))

# вариант 2 через **
def pow_num_2(x, y):
    return 1 / x ** abs(y)

print(pow_num_2(2, -3))

# вариант через цикл for
def pow_num_3(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x

print(pow_num_3(2, -3))

# задание пятое - сумма чисел строки

def sum_str_num():
    result = 0
    while True:
        numbers = input("Введите числа через пробел: ").split(" ")
        for num in numbers:
            try:
                if num == '!':
                    print("Сумма: {}. Конец".format(result))
                    return
                else:
                    result += int(num)
            except ValueError:
                print("Введите число или !")
        print("Итоговая сумма: {}".format(result))

sum_str_num()

# задание шестое - слово с заглавной буквой

# ввод - слово, вывод - слово с заглавной буквой
def int_func_1():
    while True:
        word = input("Введите слово: ")
        if not word.istitle() and word.isalpha():
            return word.capitalize()
        else:
            print("Вы ввели слово с заглавной буквы\n")

print(int_func_1())

# ввод - слова, разделенные пробелом, вывод - слова с заглавной буквы
def int_func(text):
    new_words = []
    for word in range(len(text)):
        new_words.append(text[word].title())
    return ' '.join(new_words)

def int_func_input():
    print(int_func(input("Текст: ").split(" ")))

int_func_input()




