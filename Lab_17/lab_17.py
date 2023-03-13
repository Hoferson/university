numbers = [12, 21, 3, 43, 4, 3, 7, 8645, 66, 65, 9, -1]      # 1

def function(numbers):
    result =1

    for num in numbers:
        if num < 10 and num > -10:
            # print(f'* {num}')
            result *= num
    
    return result

print(function(numbers))



mass = [3,4,6,2,7,211,89,3444,123,4533,  133,135,13,6,68456,32435,2111,5467, 55, 45]        # 2

def sort_function(mass):
    for u in range(0,10):           # range(0, len(mass)/2)
        for i in range(10, 19):     # range(len(mass)/2, len(mass)-1)
            
            if mass[i] > mass[i+1]:
                mass[i], mass[i+1] = mass[i+1], mass[i]

    return mass

print(sort_function(mass))
print(sorted(mass[10:]))