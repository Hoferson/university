numbers = [12, 21, 3, 43, 4, 3, 7, 8645, 66, 65, 9, -1]

def function(numbers):
    result =1

    for num in numbers:
        if num < 10 and num > -10:
            # print(f'* {num}')
            result *= num
    
    return result

print(function(numbers))