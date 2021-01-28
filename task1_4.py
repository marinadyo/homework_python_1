# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Enter a number: "))
small_dig = 9
large_dig = 0

while number > 0:
    x = number % 10  # раскладываем число - выводим остатки, каждый остаток сравниваем в циклах if,
    # пока цифры не заканчиваются, выводим последние знач
    if small_dig > x:
        small_dig = x
    if large_dig < x:
        large_dig = x

print("Largest digit:", large_dig)
print("Smallest digit:", small_dig)


