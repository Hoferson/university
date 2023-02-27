
mass = [3,4,6,2,7,211,89,3444,123,4533,  133,135,13,6,68456,32435,2111,5467, 55, 45]        # 1

def sort_function(mass):
    for u in range(0,10):           # range(0, len(mass)/2)            |while u < len(mass)/2:
        for i in range(10, 19):     # range(len(mass)/2, len(mass)-1)  |    u ++
            
            if mass[i] > mass[i+1]:
                mass[i], mass[i+1] = mass[i+1], mass[i]

    return mass[10:]

print(sort_function(mass))

# mass.sort()
# print(mass)                                                                      #1.1


mass = [234, 23, 345, 1, 8, 234, 678, 43, 8, 44, 244, 600]                         # 2

def find_min_paired(mass):
    result = mass[0]

    for i in mass:
        if i % 2 == 0 and i < result:
            result = i
        
    return(result)

print(find_min_paired(mass))
#print(min(mass))

mass = []
lenght = 0                                                                      # 3
while lenght <= 10:
    
    mass.append(input(f'Enter {lenght+1}th element: '))
    lenght += 1

k = input('Enter number K: ')


def sort_by_k(mass, k):
    less = []
    great = []
    equal = []
    
    for i in mass:
        if i < k:
            less.append(i)
        elif i == k:
            equal.append(i)
        else:
            great.append(i)
        
    result = {'less': less, 'great': great, 'equal': equal}
    return result

print(sort_by_k(mass, k))