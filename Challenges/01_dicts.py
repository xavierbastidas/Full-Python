'''
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario

my_dict={'Euro':'€','Dollar':'$','Yen':'¥'}
my_data = str(input("Porfavor estimado usuario ingrese una divisa : "))

print(my_dict.get(my_data.title(), "La divisa no está."))


Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y
teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.


name=str(input("Porfavor ingrese su nombre : "))
age=int(input("Porfavor ingrese su edad : "))
address=str(input("Porfavor ingrese su direccion : "))
phone=str(input("Porfavor ingrese su telefono: "))

my_dict = {"Nombre":name,
           "Edad":age,
           "Direccion":address,
           "Telefono":phone
           }
print(my_dict["Nombre"]+ " tiene " + str(my_dict["Edad"])+ 
      " ,vive en " + my_dict["Direccion"] + " y su número de teléfono es "+ my_dict["Telefono"])

'''

'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
 Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.


my_dict={
    "Plátano":1.35,
    "Manzana":0.80,
    "Pera":0.85,
    "Naranja":0.70
}

frut=str(input("Que fruta desea llevar ? "))
kl=float(input("Cuantos kilos desea llevar ? "))

if frut.title() in my_dict:
    print("Precio total : " , my_dict[frut.title()]*kl)
else:
    print(f"{frut} no se encuentra en stock")

'''
    





