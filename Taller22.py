num= int(input("Ingresa un número entero positivo : "))
if num <= 0:
    print("El número ingresado no es positivo:")
else:
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    if es_primo(num):
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")
    print("Los números primos hasta", num, "son:")
    for i in range(2, num+1):
        if es_primo(i):
            print(i)