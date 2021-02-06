# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('my_file.txt', 'w') as my_file:
    while True:
        line = input('Enter something to add to the file: ')
        if line == '':
            break
        my_file.write(line + '\n')
