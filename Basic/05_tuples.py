### Tuples ###
#Conjunto de valores
my_tuple = tuple()
my_other_tuple = ()
my_tuple = (22,1.70,"Jonathan","Bastidas","Bastidas")
my_other_tuple=(34,22,18)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Bastidas"))
print(my_tuple.index("Jonathan"))
print(my_tuple.index("Bastidas"))

#Las tuplas no pueden ser modificadas immutables
#my_tuple[1] = 1.75
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[1:3])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3]="UTA"
my_tuple.insert(1,"Azul")
my_tuple= tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple  #Eliminar la tupla 
print(my_tuple)  # NameError: name 'my_tuple' is not defined



















