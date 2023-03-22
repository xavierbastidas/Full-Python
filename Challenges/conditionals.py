'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

age=int(input("Digite su edad porfavor : "))
if age>=18:
    print(f"Estimado usuario usted es mayor de edad !")
else:
    print(f"Estimado usuario usted aún es menor de edad !")

'''
'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
 pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide 
 con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

password="camila"

my_password=input("Porfavor introduzca su clave ! ")

if password==my_password.lower():
    print("Ingresando al panel...")
else:
    print("Credenciales incorrectas")




