# 1. Реализовать скрипт, в котором должна быть
# предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv


def my_func():
    try:
        name, hours, rate, bonus = argv
        salary = int(hours) * int(rate) + int(bonus)
        print(f'Salary: {salary}')
    except ValueError:
        print('Error')


my_func()