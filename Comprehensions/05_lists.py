numbers = []
for element in range(1,11):
    numbers.append(element) #append permite agg cualquier elemento al final de la lista "
    
print(numbers)


numbers_v2 = [element *2 for element in range(1,11)] #lo mismo que el codigo de arriba pero en dos lineas
print(numbers_v2)
#-----------------------------------------------------------------
numbers = []
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i * 2 )
        
        
print(numbers)

numbers_v2 = [i*2 for i in range(1,11) if i % 2 == 0 ]
print(numbers_v2)