# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль. try accept
#

"""Деление введенных пользователем данных,
предусматривая обработку сит-ии деления на 0."""

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))


def division(x, y):
    sub = x / y

    print(sub)


try:
    division(number2, number1)
except (ValueError, ZeroDivisionError) as error:
    print(error)
