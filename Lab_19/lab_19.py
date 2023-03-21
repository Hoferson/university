matrix = [[1,1,1,1],[12,12,12,12],[2,2,2,2],[23,23,23,23],[3,3,3,3]]            # 1

def function(matrix):
    sum = 0
    count = 0
    for line in matrix:
        for num in line:
            if num >= 10 and num <= 20:
                sum += num
                count += 1

    return sum/count

print(function(matrix))


matrix = [[1,1,1,3,3],[12,12,12,90,99],[12,2,2,2,2]]            # 2

def function_2(matrix):
    minimal = 999999
    for line in matrix:
        for num in line:
            if num < minimal:
                minimal = num

    for line in (0,1,2):
        for num in (0,2,4):
            matrix[line][num] = minimal

    return matrix

print(function_2(matrix))


matrix = [[1,1,1,3],[12,12,90,99],[12,2,2,2],[9,8,7,6]] 

def function_3(matrix):
    ind = len(matrix[0])-1
    result = []

    for line in range(0,len(matrix)):
        result.append(matrix[line][ind])
        ind -= 1

    return result

print(function_3(matrix))
