import math
#ingreso de las variables
p = int(input("Ingrese el valor de verdad para p (1 para Verdadero, 0 para Falso): "))
q = int(input("Ingrese el valor de verdad para q (1 para Verdadero, 0 para Falso): "))
#verificación que cumplan la consición
while True:
    if p not in [0, 1] or q not in [0, 1]:
        print("Los valores de verdad deben ser 0 o 1, vuelve a ingresarlos")
        p = int(input("Ingrese el otra vez: "))
        q = int(input("Ingrese el otra vez: "))
    else:
        break
