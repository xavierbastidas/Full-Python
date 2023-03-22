### File Handling ###
#.txt
import os
import json
txt_file = open("Intermediate/my_file.txt","r+") #Leer y Escribir r+ w+


txt_file.write("Mi nombre es Jonathan\nMi apellido es Bastidas\n22 años\nY mi lenguaje preferido es Pyhton")

#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermediate/my_file.txt")

#.json file

json_file=open("Intermediate/my_file.json","w+")

json_test= {
           "name":"Jonathan",
           "surname":"Bastidas",
            "age":22,
            "Languages":["Python","Swift","Kotlin"],
            "website":"https://jonathan.dev"
            }

json.dump(json_test,json_file,indent=2)
#json.dump(json_test,json_file,indent=2)

json_file.close()


with open("Intermediate/my_file.json") as my_other_file:
    for line in  my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

#.csv file

import csv

csv_file=open("Intermediate/my_file.csv","w+")

csv_writer= csv.writer(csv_file)

csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Jonathan","Bastidas",22,"Python","https://jonathan.dev"])
csv_writer.writerow(["Roswell","",2,"COBOL",""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in  my_other_file.readlines():
        print(line)

# .xlsx file
#import xlrd
# .xml

import xml











