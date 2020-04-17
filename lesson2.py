# задание первое- создание списка, заполнение элементами разных типов данных, проверка типов данных

"""
list_1 = [1, {2, 3}, [4, 5], 'word', (6, 7), 8.0, {"key1": "value1", "key2": "value2"}]
for item in list_1:
    print(f'элемент {item} имеет тип данных - {type(item)}')
"""

# задание второе - обмен соседними индексами списка

"""
list_2 = input("Введите значения списка через пробел\n")
list_new_2 = list_2.split(" ")

i = 0
for item in range(int(len(list_new_2)/2)):
    list_new_2[i], list_new_2[i + 1] = list_new_2[i + 1], list_new_2[i]
    i += 2
print(list_new_2)
"""

# задание третье - времена года

"""
months = {
    "зима": (12, 1, 2),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11),
}

while True:
    month_num = int(input("Введите номер месяца\n"))
    if 1 <= month_num <= 12:
        break
    else:
        print("Вы ввели неправильное число")

for key in months.keys():
    if month_num in months[key]:
        print(key)
"""

# задание четвертое - вывести каждое слово строки на новой и пронумеровать

"""
str_1 = input("Введите строку\n")
new_str_1 = []
for word in str_1.split(" "):
    new_str_1.append(word[0:11])
for i, new_word in enumerate(new_str_1):
    print(i, new_word)
"""

# задание пятое - реализация структуры "Рейтинг"

"""
my_list = [7, 5, 3, 3, 2]
max_list_num = max(my_list)
min_list_num = min(my_list)
some_num = int(input("Введите число, которое хотите поместить\n"))
if min_list_num < some_num < max_list_num:
    my_list.insert(my_list.index(some_num - 1), some_num)
elif some_num > max_list_num:
    my_list.insert(0, some_num)
elif some_num in my_list:
    my_list.insert(my_list.index(some_num), some_num)
else:
    my_list.append(some_num)
print(my_list)
"""

# задание шестое - реализация структуры "Товары"

# не разобрался с шестым заданием(
"""
prod = input("Введите название товара\n")
price = int(input("Введите цену товара\n"))
num_count = int(input("Введите количество товара\n"))
units = input("Введите единицы товара\n")
content = {"название": prod, "цена": price, "количество": num_count, "ед": units}
print(content)
"""

