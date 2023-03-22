### Sets ###
my_set = set()
my_other_set= {}
print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario
my_other_set = {"Jonathan","Bastidas",22}
print(type(my_other_set))
print(len(my_other_set))
my_other_set.add("UTA")
print(my_other_set) # Un set no es una estructura ordenada
my_other_set.add("UTA") #Un set no admite repetidos
print(my_other_set) 

print("Jonathan" in my_other_set)
print("Jonatan" in my_other_set)

my_other_set.remove("Jonathan")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set  #Elimina el objeto 

#print(my_other_set)

my_set = {"Jonathan","Bastidas",22}
my_list  = list(my_set)
print(my_list[0])

my_other_set={"Java","C#","JavaScript"}
my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_new_set).union(my_set).union({"Kotlin","PHP"})) 

print(my_new_set.difference(my_set))





