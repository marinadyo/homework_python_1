# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна
# выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.
# #


"""Задачу получилось решить только
после просмотра кода с разбора дз"""


def my_func():
    x = 0
    while True:
        my_num = input('Enter numbers or press "Q" to exit the program: ').split()
        for num in my_num:
            if num == 'q'.upper():
                return x
            else:
                try:
                    x += int(num)
                except ValueError:
                    print('Press "Q" to exit the program!')
        print(f'Sum of all the numbers = {x}')


print(my_func())

"""До просмотра разбора получался 
вот такой вот монстр Франкенштейна"""

# first_touch = input('Press enter to continue or "Q" to exit the program: ')
# if first_touch == 'Q'.upper():
#     print('The end')
#     exit()
#
# num_string = input('Enter list of numbers with spaces: ').split()
# num_list = []
# list_sum = 0
#
# num_num = [int(x) for x in num_list]
#
# for num in num_string:
#     num_list.append(num)
#
#
# while num_list != 'Q'.upper():
#
#     def num_sum():
#         num_num = [int(x) for x in num_list]
#         x = sum(num_num)
#         return x
#
#
# print(num_sum())
# list_sum.append(num_sum())

