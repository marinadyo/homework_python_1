"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку
метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""
import numpy

# вариант1
class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def str(self):
        return '\n'.join(map(str, self.input))

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'The length is different'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'The length is different'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1 + matrix_2)

# вариант2
"""Пыталась решить задачу с помощью numpy, но не понимаю, как включить в процесс def __srt__ """


class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __add__(self, other):
        matrix = numpy.array(self.input + other.input)
        return matrix

    def __str__(self):
        return '\n'.join(map(str, self.input))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(numpy.array(matrix_1.input) + numpy.array(matrix_2.input))
