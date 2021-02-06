# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
# read lines. read len(split

with open('my_file.txt', 'r') as my_file:
    lines = my_file.readlines()
    lines_count = len(lines)
    print(f'Кол-во строк: {lines_count}')
    for i, v in enumerate(lines, start=1):
        words = len(v.split())
        print(f'В строке: {i} - {words}')