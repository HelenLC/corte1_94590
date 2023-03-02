def suma(a,b):
 resultado = a+b
 return resultado
n='si'
while n=='si':
 a=int(input('Ingrese un numero:'))
 b=int(input('Ingrese un numero:'))
 res = suma(a,b)
 print(res)
 n =input('¿Quiere sumar otro numero? (si/no)')