#ingreso de las variables
p = int(input("Ingrese el valor de verdad para p (1 para Verdadero, 0 para Falso): "))
q = int(input("Ingrese el valor de verdad para q (1 para Verdadero, 0 para Falso): "))

#verificación que cumplan la consición
while True:
    if p not in [0, 1] or q not in [0, 1]:
        print("Los valores de verdad deben ser 0 o 1, vuelve a ingresarlos")
        p = int(input("Ingrese el valor p otra vez: "))
        q = int(input("Ingrese el valor q otra vez: "))
    else:
        break

#logica de la implicación
if p == 1 and q == 0:
    implicación = 0
    print(f"p={p} (Verdadero) y q={q} -> p => q es Falso")
    print("La reciproca de p => q es q => p es Verdadera")
else:
    implicación = 1
    print(f"p={p}, q={q} -> p => q es Verdadero")
    print("La reciproca de p => q es q => p es Verdadera")

#La contrareciproca
pneg = 1 - p
qneg = 1 - q
print(f"Negación de q (~q) es: {qneg}")
print(f"Negación de p (~p) es: {pneg}")
