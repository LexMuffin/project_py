# задание первое - создание файла и запись в него

file_name = input("Название файла: ")
file_1 = open(file_name, 'w', encoding='UTF-8')
while True:
    input_data_1 = input("Содержимое: ")
    if input_data_1 == "":
        break
    file_1.write(input_data_1 + '\n')
file_1.close()


# задание второе - подсчет количества строк и символов в каждой строке

file_2 = open("text_1.txt", 'r', encoding='UTF-8')
line_1 = 0
for each_str in file_2:
    line_1 += 1
    flag_1 = 0
    word_1 = 0
    for each_letter in each_str:
        if each_letter is not " " and flag_1 == 0:
            word_1 += 1
            flag_1 = 1
        elif each_letter is " ":
            flag_1 = 0
            word_1 = 0
    print(each_str, len(each_str), "количество символов,", word_1, "слов")
print("Всего: ", line_1, "строк")

file_2.close()


# задание третье - вывести фамилии сотрудник с зп > 20000 и подсчет средней зп

from statistics import mean

file_3 = open("salaries.txt", 'r', encoding='UTF-8')
stuff_and_salaries = {}
all_salary = [] # небольшой костыль
for line_2 in file_3:
    worker, salary = line_2.split(" ")
    stuff_and_salaries[worker] = salary
    if int(salary) > 20000:
        print(worker)
print(mean(int(stuff_and_salaries[worker]) for worker in stuff_and_salaries)) # средняя зарплата


# задание четвертое - One, Two, Three, Four


file_4 = open("exe4.txt", 'r+', encoding='UTF-8')

list_1 = list()
for each_str in file_4.readlines():
    list_1.extend(each_str.split(" "))
print(list_1)

list_2 = ["Один", "Два", "Три", "Четыре"]

j = 0
for i in range(0, len(list_1), 3):
    list_1[i] = list_2[j]
    j += 1
print(list_1)

file_new_4 = open("exe4_new.txt", "w", encoding='UTF-8')
file_new_4.writelines(list_1) # вместо list_1 можно написать |" ".join(list_1)|
file_new_4.close()


# задание пятое - создание файла , запись чисел , подсчет чисел


with open("exe5.txt", 'w', encoding='UTF-8') as exe5:
    try:
        nums_input = input("Введите числа: \n")
        exe5.write(nums_input)
        sum_num = 0
        for num in nums_input.split(" "):
            sum_num += int(num)
        print(sum_num)
    except ValueError:
        print("Вы ввели не числа")


# задание шестое - создание словаря с предметами
# в голову не пришла более легкая идея или оптимальный способ для сортировки чисел

with open("exe6.txt", 'r+', encoding='UTF-8') as exe6:

    str_exe6 = exe6.read().split("\n")[:-1]

    libr_exe6 = {}
    for item in str_exe6:
        subject = item.split(" ")[0]
        num_les = item.split(" ")[1:]
        libr_exe6[subject] = num_les
    print(libr_exe6)

    for i in libr_exe6:
        list_2 = libr_exe6[i]
        list_4 = []             # в этот список будем помещать итоговые числа без пропусков, букв или символов
        for elem in list_2:
            list_3 = []
            for k in elem:
                if k in "0123456789":
                    list_3.append(k)           # здесь идет сортировка, чтобы получить только числа в списке
            list_4.append("".join(list_3))     # соединяем числа
        list_4 = [x for x in list_4 if x]      # здесь убираем пустые элементы, если таковые есть

        summ = 0
        for j in range(0, len(list_4)):  # здесь введем подсчет всех занятий(лекций, практикумов, лабы и тп)
            summ += int(list_4[j])
        print(i, summ)

# задание седьмое - вычисление прибыли компаний и средней прибыли
from statistics import mean
import json

file_7 = open("exe7.txt", 'r+', encoding='UTF-8')
firm_list_1 = file_7.read().split("\n")[:-1]
print(firm_list_1)

firm_lib_profit = {}
firm_lib_damages = {}
for i in firm_list_1:
    firm_name = i.split(" ")[0]
    revenue = int(i.split(" ")[2])
    costs = int(i.split(" ")[-1])
    profit = revenue - costs
    if profit > 0:
        firm_lib_profit[firm_name] = profit
    elif profit < 0:
        damages = profit
        firm_lib_damages[firm_name] = damages
print(firm_lib_profit)
print(firm_lib_damages)

average_profit = {}
for j in firm_lib_profit:
    mean_profit = mean(firm_lib_profit.values())
average_profit['average_profit'] = mean_profit
print(average_profit)

common_list = [firm_lib_profit, firm_lib_damages, average_profit]
print(common_list)

with open("common_list.json", 'w') as cmn_lst:
    json.dump(common_list, cmn_lst)






