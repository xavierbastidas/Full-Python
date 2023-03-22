### Lists ###
my_list= list()
my_other_list=[]
print(len(my_list))
my_list=[22,18,26,34,19,22,20]
print(my_list)
print(len(my_list))
my_other_list=[23,1.70,"Jonathan","Bastidas"]
print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(22)) #Numero de ocurrencias de un valor
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

print(my_other_list.index("Jonathan"))

age,height,name,surname= my_other_list
print(name)
name,height,age,surname= my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3]
print(age)

print(my_list+my_other_list)

#print(my_list - my_other_list)

my_other_list.append("BastidasDev")
print(my_other_list)

my_other_list.insert(1,"Rojo")

print(my_other_list)

my_other_list[1]="Azul"

print(my_other_list)

my_other_list.remove("Azul")

print(my_other_list)

my_list.remove(22)
print(my_list)


print(my_list.pop())


print(my_list)


my_pop_element= my_list.pop(2)

print(my_pop_element)

print(my_list)

print("***********")
del my_list[2]  #Elimina por indice

print(my_list)


my_new_list = my_list.copy()

print(my_list)
print(my_new_list)
my_new_list.reverse()

print(my_new_list)

my_new_list.sort() #Ordena de menor a mayor

print(my_new_list)


#Hacer sublistas

print(my_new_list[1::3])

print(my_new_list)


my_list.clear()

print(my_list)

my_list="Hola Python"

print(my_list)

print(type(my_list))

