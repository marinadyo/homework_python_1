# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# код до разбора дз
enter = input('Enter any words you like, use spaces: ').split()
for x, i in enumerate(enter, 1):
    if len(i) > 10:
        i = i[0:10]
    print(x, i)


# после разбора дз

enter = input('Enter any words you like, use spaces: ').split()
for i, x in enumerate(enter, 1):
    print(f'{i}. {x[0:10]}')