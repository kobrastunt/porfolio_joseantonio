"""
Sientase libre de utilizar el programa, copiarlo, modificarlo para sus necesidades.
Éste es un sencillo programa que nos verifica a través de los valores introducidos (cartegoría y antiguedad ) si un usuario posee la condición de socio Vip o no.
Las condiciones que se deben cumplir para ser socio Vip son:
  - Pertenecer a la categoría A ó poseer una antiguedad entre 10 y 21 años, ambos inclusive.
"""
categoria = input("Ingrese su categoría A, B o C: ").upper()

# Bucle para validar que la categoría sea algunas de las letras a, b ó c.
while categoria not in ['A', 'B', 'C']:
    print("Error: La categoría debe ser A, B o C.")
    categoria = input("Ingrese su categoría A, B o C: ").upper()

antiguedad = input("Escriba su antigüedad: ")

# Bucle para validar la antigüedad como número entero.
while not antiguedad.isdigit():
    print("Error: La antigüedad debe ser un número entero.")
    antiguedad = input("Escriba su antigüedad: ")

antiguedad = int(antiguedad)

if categoria == 'A' or (antiguedad >= 10 and antiguedad <= 21):
    print("Socio VIP")
else:
    print("No eres socio VIP")
