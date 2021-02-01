# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый
# цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import cycle

# a)
number = int(input('Enter a number: '))
for i in count(number):
    if i < 20:
        print(i)
# б)
c = 0
my_list = [1, 2, 3, 4, 5]
for i in cycle(my_list):
    if c < 10:
        print(i)
        c += 1
