'''
Ejercicio 1
Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
def print_name():
    print("¡Hola amiga!")

print_name()

Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
def print_name(name:str):
    print(f"¡hola {name}!")

Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial.
def fact(number):
    number_fact=1
    for i in range(number):
        number_fact*=number-i
    print(number_fact)
fact(5)

Ejercicio 9
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

'''

def mcd(number_one:int,number_two:int):
     i,_mcd=2,-1
     may,max=i,number_one+number_two
     for i in range(i,max):
             if number_one%i==0  and number_two%i==0:
                 if i>may:
                     _mcd=i
     return _mcd

print(mcd(80,60))


def mcm (number_one:int,number_two:int):
     max=number_one+number_two
     _mcm_one,_mcm_two,_mcm=[],[],[]
     for i in range(1,max):
         _mcm_one.append(number_one*i)
         _mcm_two.append(number_two*i)
         for number in _mcm_two:
              if number in _mcm_one:
                   _mcm.append(number)
     return min(_mcm)  

print(mcm(80,60))









