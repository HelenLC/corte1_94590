n = int(input('Ingrese un numero'))
while n != 0:
    x= (n//10)*10
    dig= n-(x*10)
    n = x
    if dig ==5:
        digit_equal += 1
        print('Salto')
    else:
        print(dig)
        digit_different += 1
print(f'iguales a 5{digit_equal}')
print(f'diferentes a 5{digit_different}')
print(f'numero de digitos{digit_equal+digit_different}')
