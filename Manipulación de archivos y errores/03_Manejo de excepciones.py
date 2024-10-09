try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

# detectar y controlar los errores sin que el programa se detenga 
try: 
    age = 10 
    if age < 18:
        raise Exception("No se permiten menores de edad")
except Exception as error:
    print(error)


try:
    assert 1 != 1, "uno es igual que uno"
except ArithmeticError as error:
    print(error)

print("hola")