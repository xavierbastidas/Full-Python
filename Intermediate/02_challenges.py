### Challenges ###
''' 
Reto #0: EL FAMOSO "FIZZ BUZZ”
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
def fizzbuzz():
    for i in range(1,101):
        if i%3==0  and i%5==0:
           print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
fizzbuzz()

'''

'''
Reto #1: EL "LENGUAJE HACKER"
 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''


language_leet = {
    'A':'4',
    'B':'I3',
    'C':'[',
    'D':')',
    'E':'3',
    'F':'|=',
    'G':'&',
    'H':'#',
    'I':'1',
    'J':',_|',
    'K':'>|',
    'L':'1',
    'M':'/\/\'',
    'N':'^/',
    'O':'0',
    'P':'|*',
    'Q':'(_,)',
    'R':'I2',
    'S':'5',
    'T':'7',
    'U':'(_)',
    'V':'\/',
    'W':'\/\/',
    'X':'><',
    'Y':'j',
    'Z':'2',
}
language_leet_two = {
    'A':'4',
    'B':'8',
    'C':'C',
    'D':'D',
    'E':'3',
    'F':'F',
    'G':'6',
    'H':'H',
    'I':'1',
    'J':'J',
    'K':'>|',
    'L':'L',
    'M':'M',
    'N':'N',
    'O':'0',
    'P':'9',
    'Q':'Q',
    'R':'R',
    'S':'5',
    'T':'7',
    'U':'U',
    'V':'V',
    'W':'\/\/',
    'X':'><',
    'Y':'j',
    'Z':'2',
}

def leet(word:str):
    transl_word=" "
    for index in word:
       if index==" ":
            transl_word+=index
       else:
          for value in language_leet_two[index.title()]:
               transl_word+=value
    return transl_word

word=input(str("Porfavor ingrese un texto : "))

print(leet(word))



















