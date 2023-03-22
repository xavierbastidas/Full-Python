### List Comprehension ###
my_original_list=[0,1,2,3,4,5,6,7]
print(my_original_list)
my_range =range(8)
print(list(my_range))

#Crea listas que operamos en el momento que creamos
#Estamos modificando el valor antes de guardar
#my_list = [i for i in "SALUDOS"]

my_list = [i for i in range(8)]
print(my_list)

my_list = [i*2 for i in range(8)]
print(my_list)

my_list = [i*i for i in range(8)]
print(my_list)

def sum_five(number):
    return number+5

my_list = [sum_five(i) for i in range(8)]
print(my_list)


