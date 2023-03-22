### Classes ###

class MyEmptyPerson:
    pass
   

#print(MyEmptyPerson())

class Person:
    def __init__(self,name,surname,alias="Sin alias") :
        self.full_name=f"{name} {surname} {alias}"
        self.__name=name  #Propiedad privada

    
    def get_name(self):
       return self.__name
    
    def set_name(self,name):
        self.__name=name

    def walk(self):
        print(f"{self.full_name} Esta caminando")
    


my_person=Person("Jonathan","Bastidas")

print(my_person.full_name)

#print(my_person.__name )

print("######")


my_person.set_name("Carlos")

print(my_person.get_name())

my_person.walk()

my_other_person=Person("Jonathan " ,"Bastidas" ,"JonathanDev")

print(my_other_person.full_name)

my_other_person.walk()

my_other_person.full_name="Héctor de León El loco de los perros"

print(my_other_person.full_name)


my_other_person.full_name=67457

print(my_other_person.full_name)













