cadena = 'Hola mundo'
print(cadena[6])
print(len(cadena))
texto=''

#accediendo con un for
for i in cadena:
    texto += str(f'{i},')
    print(texto)

    #accediento con un while
    contador = 0
    texto2 =''

    while contador < len(cadena):
        texto2 += str(f'{i},')
        contador +=1
    print(texto2)