###  Loops ###

#While

my_condition = 0

while  my_condition <10:
    print(my_condition)
    my_condition+=2
else:                            #Pertenece al while
    print("Mi condición  es mayor o igual que 10")

    
    
while  my_condition <20:
     my_condition+=1
     if my_condition==15:
         print("Se detiene la ejecucion ")
         break
     print(my_condition)

print("La ejecución continúa")


#For

my_list=[35,24,62,52,30,30,17]

for element  in my_list:
    print(element)

my_tuple = (22,1.70,"Jonathan","Bastidas","Bastidas")

for element  in my_tuple:
    print(element)


my_set = {"Jonathan","Bastidas",22}


for element  in my_set:
    print(element)


my_dict={"Nombre":"Jonathan",
         "Apellido":"Bastidas",
         "Edad":22,
         "Lenguajes":{"Python","Swift","Kotlin"},
         1:1.70
         }



print("######################")

for element  in my_dict:
    print(element)
    if element=="Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")

print("La ejecución continúa")
#elif no funciona en el for


print("######################")

for element  in my_dict:
    print(element)
    if element=="Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")



for i in range(10):
    print(i+1)

