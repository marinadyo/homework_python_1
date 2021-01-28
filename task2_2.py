# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# мой код до разбора дз
any_list = []
i = 0
while i <= 4:
    x = int(input('Enter 5 numbers to your list: '))
    any_list.append(x)
    i += 1

x = 0
for i in range(int(len(any_list) / 2)):
    any_list[x], any_list[x + 1] = any_list[x + 1], any_list[x]
    x += 2
print(any_list)

# мой код после разбора дз
any_list = list(input('Enter five numbers: ').split())
for x in range(1, len(any_list), 2):
    any_list[x - 1], any_list[x] = any_list[x], any_list[x - 1]
print(any_list)
