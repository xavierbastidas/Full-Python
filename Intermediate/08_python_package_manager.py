### Python Package Manager ###
#pip https://pypi.org/
import  numpy,pandas,requests
print(numpy.version.version)
numpy_array=numpy.array([23,50,80,90,56,23,12])
print(type(numpy_array))
print(numpy_array*2)
#pip list
#pip uninstall pandas
#pip show numpy

response =requests.get("https://pokeapi.co/api/v2/pokemon?limited=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package
from my_package import arithmetics

print(arithmetics.sum_two_values(1,4))




