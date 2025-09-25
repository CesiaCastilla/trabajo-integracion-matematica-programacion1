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
    implicacion = 0
    print(f"p={p} y q={q} -> p => q es Falso")
else:
    implicacion = 1
    print(f"p={p}, q={q} -> p => q es Verdadero")

#La reciproca
if q == 1 and p == 0:
    reciproca = 0
    print("La recíproca q => p es Falsa")
else:
    reciproca = 1
    print("La recíproca q => p es Verdadera")
    
#La contrareciproca
pneg = 1 - p
qneg = 1 - q
print(f"Negación de q (~q) es: {qneg}")
print(f"Negación de p (~p) es: {pneg}")
if qneg == 1 and pneg == 0:
    contrarreciproca = 0
    print(f"~q={qneg} y ~p={pneg} -> ~q => ~p es Falso (0)")
else:
    contrarreciproca = 1
    print(f"~q={qneg}, ~p={pneg} -> ~q => ~p es Verdadero (1)")
        
print(f"Resultado final de ~q => ~p: {contrarreciproca}")

#Verificación de resultados
print("\n--- Comparación de Resultados ---")
print(f"Resultado de la implicación (p => q): {implicacion}")
print(f"Resultado de la contrarrecíproca (q => p): {reciproca}")
print(f"Resultado de la contrarrecíproca (~q => ~p): {contrarreciproca}")

if implicacion == contrarreciproca:
    print("\n¡Ambas proposiciones son lógicamente equivalentes!")
    print("Esto se conoce como el Principio de Contraposición en Lógica.")
else:
    print("\nLas proposiciones NO son lógicamente equivalentes.")

if implicacion == reciproca:
    print("\n¡Ambas proposiciones son lógicamente equivalentes!")
    print("Esto se conoce como equivalencia lógica o bicondicional.")
else:
    print("\nLas proposiciones NO son lógicamente equivalentes.")
