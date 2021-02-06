# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

with open('num_file.txt', 'w+') as num_file:
    num = input('Enter your numbers with splits: ')
    num_file.write(num + '\n')
    num = map(int, num.split())
    num_sum = sum(num)
    num_file.write(str(num_sum))
    print(num_sum)
