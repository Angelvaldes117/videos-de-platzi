# union para unir 
set_a = {"col" , "mex" , "bol"}
set_b = {"pe" , "bol"}

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b) # | para unir los conjuntos, lo cual automáticamente elimina los duplicado


#intersection para buscar los mismo paises 
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)


#difference solo utiliza los que no estan repetido en el a y b 
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#  symmetric_difference no utilisa los elementos en comun 

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)