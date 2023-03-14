n=int(input('Ingrese la cantidad de numeros que quiere visualizar'))
a =0; b=1
print(a,'\n',b)
for i in range(n-2):
    c= a+b
    a= b
    b= c
    print(c)          