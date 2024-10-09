with open('./Texto.txt', "r+") as file:
    for line in file:
        print(line)
    file.write("que lindo dia hace hoy\n")
    file.write("otras lineas de texto1")
    file.write("otras lineas de texto3")