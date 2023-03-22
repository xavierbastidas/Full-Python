### Functions ###

def my_function():
    print("Esto es una función")
   

my_function()
my_function()
my_function()

def sum_two_values(first_number:int,second_number:int):
    print(first_number+second_number)

sum_two_values(5,7)
sum_two_values(53342,3431)
sum_two_values("5","7")
sum_two_values(1.4,5.2)

#Retorno de valores en una funcion

def sum_two_values_with(first_number:int,second_number:int):
    return first_number+second_number


my_result =sum_two_values_with(100,34)

print(my_result)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name(surname="Bastidas",name="Jonathan")

def print_name_with_default(name,surname,alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Jonathan","Bastidas","JonathanDev")
print_name_with_default("Jonathan","Bastidas")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_upper_texts("Hola","Python","JonathanDev")















































