###  Exception Handing ###
number_one =5
number_two =1
number_two ="1"

# try except
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error : No se pueden sumar str e int")

# try except else finally
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error : No se pueden sumar str e int")
else: #Opcional
    #Se ejecuta si no produce una excepcion
    print("La ejecución continúa correctamente")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continúa ")

#Captura de la informacion de la excepcion

try:
    print(number_one+number_two)
    print("No se ha producido un error")
except ValueError as error:
    #Se ejecuta sis e produce una excepcion
    print(error) 
except Exception as error:
    #Se ejecuta sis e produce una excepcion
    print(error)


