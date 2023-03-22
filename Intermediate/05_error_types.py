### Error Types ###

#SyntaxError
#print "!Hola comunidad!" #Descomentar para Error
print("!Hola comunidad!")

#NameError
#NameError: name 'name' is not defined
language="Spanish" #Comentar para Error
print(language)

#IndexError
#IndexError: list index out of range
my_list=["Pyhton","Swft","Kotlin","Dart","JavaScript"]
print(my_list[4])
# print(my_list[5]) #Descomentar para Error

#ModuleNotFoundError
import math

#AttributeError
#module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

#KeyError

my_dict = {"Nombre":"Jonathan",
                 "Apellido":"Bastidas",
                 "Edad":22,
                 1:"Python"}

print(my_dict["Edad"])
#print(my_dict["Apelido"]) #Descomentar para Error
print(my_dict["Apellido"])

#TypeError
#list indices must be integers or slices, not st
#print(my_list["0"])
print(my_list[0])
print(my_list[False])


#ImportError
# cannot import name 'PI' from 'math' (unknown location)

from math import pi

#ValueError: invalid literal 
my_int=int("10")
#my_int=int("10 Años")
print(type((my_int)))

#ZeroDivisionError : division by zero
#print(4/0)
print(4/1)    










