# 5. Реализовать формирование списка, используя
# функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
#

from functools import reduce

my_list = [num for num in range(99, 1001) if num % 2 == 0]
result = reduce(lambda x, y: x * y, my_list)
print(result)
