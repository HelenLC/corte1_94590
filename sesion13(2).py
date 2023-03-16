n = input('Ingrese un numero')

dimension = len(n)
contador=0

if 2< dimension <8:
    for i in n:
        if i =='5':
            print('salto')
            contador += 1
        else:
            print(i)
    print(f'numros iguales a 5:{contador}')
    print(f'numros diferentes a 5:{dimension-contador}')
    print(f'total de digitos:{dimension}')

else:
    print("error, fuera de rango")
