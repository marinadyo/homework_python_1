# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

c = input('Enter any number: ')
a = str(c + c)
b = str(c + c + c)
d = int(c) + int(a) + int(b)
print(d)
