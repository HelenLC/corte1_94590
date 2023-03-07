from factorial import fcn_factorial as f 

def main():
    n=int(input('Ingrese el numero de grupos:'))
    m=int(input('Ingrese el numero de muestra:'))
    result =((f(n))/(f(m))*f(n-m))
    print(f'El numero de convinaciones posibles es:'{result})
 

