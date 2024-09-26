set_countries = {"mex , pan , col "}
print(set_countries)        
print(type(set_countries))

#----------------------------------------------------

set_numbers = { 1 , 2 , 4 , 3 , 332}
print(set_numbers)

set_numbers = { 1,1 , 2 , 4 ,4, 3 , 3}
print(set_numbers)   

#---------------------------------------------------

set_types = { 1 , "hola" , False , 12.12 }
print(set_types)


#--------------------------------------------------

set_from_string = set("hoola")
print(set_from_string)

set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)

#-------------------------------------------------

numbers = [1,2,3,4,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)


#SEGUNDO VIDEO

set_countries = { "mex" , "chil" , "arg"}
size = len(set_countries)
print(size)

print("mex" in set_countries)
print("pe" in set_countries)
#---------------------------------------------------

# add ayuda a agregar un elemento al conjunto
set_countries.add("pe")
print(set_countries)

#----------------------------------------------------

#update ayuda a actualisar un conjunto 
set_countries.update({"ven","ecu","pe"})
print(set_countries)

#-----------------------------------------------------

# remove , descard y clear ayuda a eleminar

set_countries.remove("arg")
print(set_countries)

set_countries.discard("ar")
print(set_countries)

set_countries.clear()
print(set_countries)
