# 4. Программа принимает действительное положительное
# число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


"""Два варианта решения задачи: возведение в степень"""


# 1.
def my_func(x, y):
    z = x ** y
    return z.__round__(4)


print(my_func(3, -3))


# 2.
def my_func(x, y):
    if y == 0:
        return 1
    if y < 0:
        return 1 / my_func(x, -y)

    return x * my_func(x, y - 1)


print(my_func(2, -3))
