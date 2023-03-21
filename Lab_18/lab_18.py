matrix = [[34,5,6,76],[1,4,3,1],[44,45,65,9],[90,99,1,1],[22,2,222,22]]             # 1

def function(matrix):
    minimal = 9999999
    matrix_sum = 0
    lenght = 0
    for line in matrix:
        lenght += len(line)             # Подсчет сумарной длинны всех строчек матрицы
        for num in line:
            matrix_sum += num           # Подсчет суммы всех элементов матрицы
            if num < minimal:           # Нахождение минимального элемента
                minimal = num
    #print(lenght, '  ', minimal, '  ', matrix_sum)
    return minimal * (matrix_sum/lenght)


print(function(matrix))







matrix = [[34,5,6,76,67],[1,4,3,1,7],[44,45,65,9,43],[90,99,1,1,56],[22,2,222,22, 2], [1, 11, 111, 112, 9]]             # 2

def function_2(matrix):
    maximal = 0
    for line in matrix:
        for num in line:
            if num > maximal:                      # Нахождение максимального элемента
                maximal = num
                line_index = matrix.index(line)    # Запись индекса строки текущего максимального элемента

    return matrix[line_index]

print(function_2(matrix))







matrix = [[3,4,4],[0,1,2],[7,8,9],[4,5,4],[1,2,3]]              # 3

def function_3(matrix):
    percents = {}
    for line in matrix:
        for num in line:
            if num not in percents:                             # Запись елементов и их количества в словарь
                percents[num] = 1
            else:
                percents[num] += 1

    for element in percents:                                    # Расчет процентного соотношения
        percents[element] = round((percents[element]*100)/15, 2)    # round() - Функция округления

    return percents

print(function_3(matrix))

def matrix_enter():                                             # Функция ввода матрицы
    matrix = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for line in (0,1,2,3,4):
        for num in (0,1,2):
            inp = int(input('Enter a number'))
            if inp >= 0 and inp <=9:
                matrix[line][num] = inp
            else:
                print('Numbers must be 0 <= number <= 9')

    return matrix

print(matrix_enter())