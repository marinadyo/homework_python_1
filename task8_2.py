# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

try:
    if y == 0:
        raise MyException('Can not divide by 0.')
    else:
        print(x / y)
except MyException:
    print('Restart the program and try again')
