# print(0 / 0)
# print(result)
print("hola")

suma = lambda x,y: x + y 
assert suma(2,2) == 4 

print("hola 2") 

age = 17
if age < 18:
    raise Exception("no se permiten menores de edad")