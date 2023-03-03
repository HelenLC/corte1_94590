num= int(input("Ingresa un número entero: "))
if num < 0:
    print("El número ingresado no puede ser negativo.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}")