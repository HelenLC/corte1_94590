def Area(r):
  pi=3.1416
  A=pi*(r**2)
  return A

def Volumen(h,A):

  A=Area(r)
  V=A*h
  return V

r=int(input('ingrese el valor del radio'))
h=int(input('Ingrese el valor de la altura'))

A = Area(r)
V =Volumen(h,r)

print(f'el area es {A} y el volumen es {V}')